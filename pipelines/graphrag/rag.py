"""Microsoft GraphRAG 3.2: LLM graph extraction + community reports at index time,
local search at query time. Settings come from `graphrag init`, with three changes:
Haiku 4.5 through LiteLLM's Anthropic provider, the shared bge-small model served
over an OpenAI-compatible endpoint (scripts/embed_server.py), and entity types
suited to software documentation instead of the news-style defaults."""
import asyncio
import os
import subprocess
import sys
from pathlib import Path

import pandas as pd
import yaml
from graphrag import api
from graphrag.config.load_config import load_config

from harness import SETTINGS

ROOT = Path.home() / "ragbench" / "graphrag" / os.environ.get("RAGBENCH_COLLECTION", "graphrag")
ENTITY_TYPES = ["software", "command", "configuration option", "file", "concept", "organization"]


def configure():
    if not (ROOT / "settings.yaml").exists():
        subprocess.run([str(Path(sys.executable).parent / "graphrag"), "init", "--root", str(ROOT),
                        "-m", SETTINGS["llm"], "-e", "bge-small-en-v1.5"], check=True, capture_output=True)
    cfg = yaml.safe_load((ROOT / "settings.yaml").read_text())
    chat = cfg["completion_models"]["default_completion_model"]
    chat.update(model_provider="anthropic", api_base=os.environ["ANTHROPIC_BASE_URL"],
                api_key="${ANTHROPIC_API_KEY}",  # resolved from the environment, never written to disk
                call_args={"temperature": SETTINGS["temperature"], "max_tokens": 4096})
    # Community reports can run past 4,096 output tokens; a truncated report fails to
    # parse and GraphRAG keeps retrying it. Give that step its own, larger budget.
    report = dict(chat, call_args={"temperature": SETTINGS["temperature"], "max_tokens": 8192})
    cfg["completion_models"]["report_model"] = report
    cfg["community_reports"]["completion_model_id"] = "report_model"
    cfg["embedding_models"]["default_embedding_model"].update(
        model_provider="openai", api_base="http://127.0.0.1:8790/v1", api_key="local")
    cfg["extract_graph"]["entity_types"] = ENTITY_TYPES
    cfg["vector_store"]["vector_size"] = 384  # default is 3072 (OpenAI text-embedding-3-large)
    (ROOT / "settings.yaml").write_text(yaml.safe_dump(cfg, sort_keys=False))
    return load_config(ROOT)


config = configure()
tables = None


def build_index(docs):
    docs_df = pd.DataFrame({"id": [str(i) for i in range(len(docs))], "title": [d["url"] for d in docs],
                            "text": [d["text"] for d in docs]})
    results = asyncio.run(api.build_index(config=config, input_documents=docs_df))
    failed = [r.workflow for r in results if r.error]
    if failed:
        raise RuntimeError(f"GraphRAG workflows failed: {failed}")


def load_tables():
    out = ROOT / "output"
    names = ["entities", "communities", "community_reports", "text_units", "relationships", "documents"]
    return {n: pd.read_parquet(out / f"{n}.parquet") for n in names}


def answer(question):
    global tables
    tables = tables or load_tables()
    response, context = asyncio.run(api.local_search(
        config=config, entities=tables["entities"], communities=tables["communities"],
        community_reports=tables["community_reports"], text_units=tables["text_units"],
        relationships=tables["relationships"], covariates=None, community_level=2,
        response_type="Multiple Paragraphs", query=question,
    ))
    sources = context.get("sources", pd.DataFrame()) if isinstance(context, dict) else pd.DataFrame()
    doc_url = dict(zip(tables["documents"]["id"], tables["documents"]["title"]))
    unit_doc = {r.id: (list(r.document_ids) or [None])[0] if "document_ids" in tables["text_units"] else r.document_id
                for r in tables["text_units"].itertuples()}
    contexts = []
    for row in sources.itertuples():
        unit = tables["text_units"][tables["text_units"]["human_readable_id"].astype(str) == str(row.id)]
        uid = unit["id"].iloc[0] if len(unit) else None
        contexts.append({"text": row.text, "url": doc_url.get(unit_doc.get(uid), "")})
    return {"answer": response if isinstance(response, str) else str(response), "contexts": contexts}
