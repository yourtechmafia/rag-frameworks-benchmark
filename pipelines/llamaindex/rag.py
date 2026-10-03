"""LlamaIndex 0.14 RAG: VectorStoreIndex over Qdrant with a query engine."""
import os

import qdrant_client
from llama_index.core import Document, PromptTemplate, Settings, StorageContext, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.anthropic import Anthropic
from llama_index.vector_stores.qdrant import QdrantVectorStore

from harness import PROMPT, SETTINGS

COLLECTION = os.environ.get("RAGBENCH_COLLECTION", "llamaindex")
Settings.llm = Anthropic(model=SETTINGS["llm"], temperature=SETTINGS["temperature"], max_tokens=SETTINGS["max_tokens"])
# query_instruction matches the prefix every other pipeline uses (LlamaIndex adds a BGE prefix by default).
# cache_folder: LlamaIndex otherwise keeps its own model cache and downloads bge-small a second time.
Settings.embed_model = HuggingFaceEmbedding(
    model_name=SETTINGS["embedding_model"], query_instruction=SETTINGS["query_prefix"],
    cache_folder=os.path.expanduser("~/.cache/huggingface/hub"),
)
# tokenizer=list makes the splitter count characters, matching the other pipelines.
Settings.node_parser = SentenceSplitter(
    chunk_size=SETTINGS["chunk_size_chars"], chunk_overlap=SETTINGS["chunk_overlap_chars"], tokenizer=list
)
vector_store = QdrantVectorStore(client=qdrant_client.QdrantClient(url=SETTINGS["qdrant_url"]), collection_name=COLLECTION)
qa_template = PromptTemplate(PROMPT.replace("{context}", "{context_str}").replace("{question}", "{query_str}"))
engine = None


def build_index(docs):
    global engine
    if vector_store.client.collection_exists(COLLECTION):
        vector_store.client.delete_collection(COLLECTION)
    documents = [
        # Keep the URL out of the embedded text and the prompt, like the other pipelines.
        Document(text=d["text"], metadata={"url": d["url"]},
                 excluded_embed_metadata_keys=["url"], excluded_llm_metadata_keys=["url"])
        for d in docs
    ]
    index = VectorStoreIndex.from_documents(
        documents, storage_context=StorageContext.from_defaults(vector_store=vector_store)
    )
    engine = index.as_query_engine(similarity_top_k=SETTINGS["top_k"], text_qa_template=qa_template)


def answer(question):
    global engine
    if engine is None:
        index = VectorStoreIndex.from_vector_store(vector_store)
        engine = index.as_query_engine(similarity_top_k=SETTINGS["top_k"], text_qa_template=qa_template)
    response = engine.query(question)
    return {"answer": str(response),
            "contexts": [{"text": n.node.get_content(), "url": n.node.metadata["url"]} for n in response.source_nodes]}
