"""Haystack 3.x RAG: an indexing pipeline and a query pipeline over Qdrant."""
import os

from haystack import Document, Pipeline
from haystack.components.builders import ChatPromptBuilder
from haystack.components.preprocessors import RecursiveDocumentSplitter
from haystack.components.writers import DocumentWriter
from haystack.dataclasses import ChatMessage
from haystack.document_stores.types import DuplicatePolicy
from haystack_integrations.components.embedders.sentence_transformers import (
    SentenceTransformersDocumentEmbedder,
    SentenceTransformersTextEmbedder,
)
from haystack_integrations.components.generators.anthropic import AnthropicChatGenerator
from haystack_integrations.components.retrievers.qdrant import QdrantEmbeddingRetriever
from haystack_integrations.document_stores.qdrant import QdrantDocumentStore

from harness import PROMPT, SETTINGS

COLLECTION = os.environ.get("RAGBENCH_COLLECTION", "haystack")
store = QdrantDocumentStore(url=SETTINGS["qdrant_url"], index=COLLECTION, embedding_dim=384, similarity="cosine")

template = [ChatMessage.from_user(
    PROMPT.replace("{context}", "{% for d in documents %}{{ d.content }}\n\n{% endfor %}")
          .replace("{question}", "{{ question }}")
)]
query = Pipeline()
query.add_component("embedder", SentenceTransformersTextEmbedder(
    model=SETTINGS["embedding_model"], prefix=SETTINGS["query_prefix"], progress_bar=False))
query.add_component("retriever", QdrantEmbeddingRetriever(document_store=store, top_k=SETTINGS["top_k"]))
query.add_component("prompt", ChatPromptBuilder(template=template, required_variables=["documents", "question"]))
query.add_component("llm", AnthropicChatGenerator(
    model=SETTINGS["llm"],
    generation_kwargs={"temperature": SETTINGS["temperature"], "max_tokens": SETTINGS["max_tokens"]},
))
query.connect("embedder.embedding", "retriever.query_embedding")
query.connect("retriever.documents", "prompt.documents")
query.connect("prompt.prompt", "llm.messages")


def build_index(docs):
    fresh = QdrantDocumentStore(url=SETTINGS["qdrant_url"], index=COLLECTION, embedding_dim=384,
                                similarity="cosine", recreate_index=True)
    indexing = Pipeline()
    indexing.add_component("splitter", RecursiveDocumentSplitter(
        split_length=SETTINGS["chunk_size_chars"], split_overlap=SETTINGS["chunk_overlap_chars"], split_unit="char"))
    indexing.add_component("embedder", SentenceTransformersDocumentEmbedder(model=SETTINGS["embedding_model"]))
    indexing.add_component("writer", DocumentWriter(document_store=fresh, policy=DuplicatePolicy.OVERWRITE))
    indexing.connect("splitter", "embedder")
    indexing.connect("embedder", "writer")
    indexing.run({"splitter": {"documents": [Document(content=d["text"], meta={"url": d["url"]}) for d in docs]}})


def answer(question):
    result = query.run(
        {"embedder": {"text": question}, "prompt": {"question": question}},
        include_outputs_from={"retriever"},
    )
    docs = result["retriever"]["documents"]
    return {"answer": result["llm"]["replies"][0].text,
            "contexts": [{"text": d.content, "url": d.meta["url"]} for d in docs]}
