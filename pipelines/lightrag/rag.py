"""LightRAG 1.5 (graph RAG): LLM entity/relation extraction at index time, 'mix'
retrieval (knowledge graph + vector chunks) at query time. LightRAG's own
retrieval defaults and prompts are kept; only the LLM and embedding model match
the other pipelines."""
import asyncio
import os
from pathlib import Path

import numpy as np
from lightrag import LightRAG, QueryParam
from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.llm.anthropic import anthropic_complete
from lightrag.utils import EmbeddingFunc
from sentence_transformers import SentenceTransformer

from harness import SETTINGS

WORKDIR = Path.home() / "ragbench" / "lightrag" / os.environ.get("RAGBENCH_COLLECTION", "lightrag")
WORKDIR.mkdir(parents=True, exist_ok=True)
model = SentenceTransformer(SETTINGS["embedding_model"], device="cpu")  # MPS crashes inside asyncio worker threads


async def embed(texts, context="document"):
    prefix = SETTINGS["query_prefix"] if context == "query" else ""
    return np.array(model.encode([prefix + t for t in texts], batch_size=32))


loop = asyncio.new_event_loop()
rag = LightRAG(
    working_dir=str(WORKDIR),
    llm_model_func=anthropic_complete,
    llm_model_name=SETTINGS["llm"],
    llm_model_kwargs={"temperature": SETTINGS["temperature"]},
    embedding_func=EmbeddingFunc(embedding_dim=384, max_token_size=512, func=embed, supports_asymmetric=True),
    enable_llm_cache=False,  # no cached answers between benchmark runs
)
loop.run_until_complete(rag.initialize_storages())
loop.run_until_complete(initialize_pipeline_status())


def build_index(docs):
    loop.run_until_complete(rag.ainsert([d["text"] for d in docs], file_paths=[d["url"] for d in docs]))


def answer(question):
    result = loop.run_until_complete(rag.aquery_llm(question, param=QueryParam(mode="mix")))
    chunks = result.get("data", {}).get("chunks", [])
    return {"answer": result["llm_response"]["content"] or "",
            "contexts": [{"text": c.get("content", ""), "url": c.get("file_path", "")} for c in chunks]}
