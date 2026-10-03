"""DSPy 3.x RAG: a dspy.Module with a typed signature. DSPy ships no splitter or
vector store client, so retrieval uses sentence-transformers and qdrant-client directly."""
import os
import uuid

import numpy  # noqa: F401  must load before dspy: DSPy 3.4.0's lazy numpy proxy breaks qdrant-client's import
import dspy
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

from harness import SETTINGS

COLLECTION = os.environ.get("RAGBENCH_COLLECTION", "dspy")
embedder = SentenceTransformer(SETTINGS["embedding_model"])
qdrant = QdrantClient(url=SETTINGS["qdrant_url"])
dspy.configure(lm=dspy.LM(f"anthropic/{SETTINGS['llm']}", temperature=SETTINGS["temperature"],
                          max_tokens=SETTINGS["max_tokens"], cache=False))


def split(text, size=SETTINGS["chunk_size_chars"], overlap=SETTINGS["chunk_overlap_chars"]):
    """Pack paragraphs into chunks of at most `size` characters, carrying `overlap`
    characters from the end of each chunk into the next."""
    chunks, current = [], ""
    for para in text.split("\n\n"):
        while len(para) > size:  # hard-split paragraphs that are too long on their own
            para_head, para = para[:size], para[size - overlap:]
            if current:
                chunks.append(current)
                current = ""
            chunks.append(para_head)
        if current and len(current) + len(para) + 2 > size:
            chunks.append(current)
            current = current[-overlap:]
        current = f"{current}\n\n{para}" if current else para
    if current.strip():
        chunks.append(current)
    return chunks


def build_index(docs):
    chunks = [(c, d["url"]) for d in docs for c in split(d["text"])]
    vectors = embedder.encode([c for c, _ in chunks], batch_size=32)
    if qdrant.collection_exists(COLLECTION):
        qdrant.delete_collection(COLLECTION)
    qdrant.create_collection(COLLECTION, vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE))
    qdrant.upload_points(COLLECTION, [
        models.PointStruct(id=str(uuid.uuid4()), vector=v.tolist(), payload={"text": c, "url": u})
        for (c, u), v in zip(chunks, vectors)
    ])


class AnswerFromContext(dspy.Signature):
    """Answer the question using only the context. If the context does not contain the answer, say "I don't know." Keep the answer under 120 words."""

    context: list[str] = dspy.InputField()
    question: str = dspy.InputField()
    answer: str = dspy.OutputField()


class RAG(dspy.Module):
    def __init__(self):
        self.respond = dspy.Predict(AnswerFromContext)

    def forward(self, question):
        vector = embedder.encode(SETTINGS["query_prefix"] + question).tolist()
        self.hits = qdrant.query_points(COLLECTION, query=vector, limit=SETTINGS["top_k"]).points
        return self.respond(context=[h.payload["text"] for h in self.hits], question=question)


rag = RAG()


def answer(question):
    pred = rag(question=question)
    return {"answer": pred.answer,
            "contexts": [{"text": h.payload["text"], "url": h.payload["url"]} for h in rag.hits]}
