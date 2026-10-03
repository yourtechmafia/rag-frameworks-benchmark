"""Plain-Python RAG: sentence-transformers + qdrant-client + the Anthropic SDK."""
import os
import uuid

import anthropic
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

from harness import PROMPT, SETTINGS

COLLECTION = os.environ.get("RAGBENCH_COLLECTION", "baseline")
embedder = SentenceTransformer(SETTINGS["embedding_model"])
qdrant = QdrantClient(url=SETTINGS["qdrant_url"])
llm = anthropic.Anthropic()


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
    qdrant.create_collection(
        COLLECTION, vectors_config=models.VectorParams(size=len(vectors[0]), distance=models.Distance.COSINE)
    )
    qdrant.upload_points(COLLECTION, [
        models.PointStruct(id=str(uuid.uuid4()), vector=v.tolist(), payload={"text": c, "url": u})
        for (c, u), v in zip(chunks, vectors)
    ])


def answer(question):
    vector = embedder.encode(SETTINGS["query_prefix"] + question).tolist()
    hits = qdrant.query_points(COLLECTION, query=vector, limit=SETTINGS["top_k"]).points
    context = "\n\n".join(h.payload["text"] for h in hits)
    msg = llm.messages.create(
        model=SETTINGS["llm"],
        max_tokens=SETTINGS["max_tokens"],
        extra_body={"temperature": SETTINGS["temperature"]},  # SDK 1.x dropped the temperature kwarg
        messages=[{"role": "user", "content": PROMPT.format(context=context, question=question)}],
    )
    return {"answer": msg.content[0].text,
            "contexts": [{"text": h.payload["text"], "url": h.payload["url"]} for h in hits]}
