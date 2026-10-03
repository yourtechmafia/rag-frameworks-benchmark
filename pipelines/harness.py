"""Shared benchmark harness. Not counted in any framework's line count.

Each framework lives in pipelines/<name>/rag.py and exposes:
    build_index(docs: list[dict]) -> None   # docs: {"text", "url", "title"}
    answer(question: str) -> dict           # {"answer": str, "contexts": [{"text", "url"}]}

The harness times imports, indexing and every query, writes one JSONL row per
question, and tags Anthropic calls with a phase so the spend ledger can report
tokens per framework and run.

Usage (from the repo root, inside the framework's venv):
    python pipelines/harness.py langchain --variant clean --runs 3 [--limit 10] [--reindex]
"""
import argparse
import csv
import importlib
import json
import os
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PHASE_FILE = Path(os.environ.get("BENCH_PHASE_FILE", Path.home() / "ragbench" / "phase.txt"))

# Settings shared by every pipeline. Each rag.py reads them from here.
SETTINGS = {
    "llm": "claude-haiku-4-5",
    "temperature": 0,
    "max_tokens": 512,
    "embedding_model": "BAAI/bge-small-en-v1.5",
    # BGE's recommended query prefix. LlamaIndex adds it by default and cannot turn it
    # off with query_instruction="", so every pipeline uses it.
    "query_prefix": "Represent this question for searching relevant passages: ",
    "chunk_size_chars": 800,
    "chunk_overlap_chars": 100,
    "top_k": 5,
    "qdrant_url": "http://127.0.0.1:6333",
}

PROMPT = """Answer the question using only the context below. If the context does not contain the answer, say "I don't know." Keep the answer under 120 words.

Context:
{context}

Question: {question}"""


def set_phase(name: str) -> None:
    PHASE_FILE.write_text(name)


def load_docs(variant: str, subset: str | None = None) -> list[dict]:
    """variant: 'clean' (cleaned ScrapingBee markdown), 'markdown' (raw ScrapingBee
    markdown) or 'default' (BeautifulSoup get_text() of a plain GET, which is what
    LangChain's WebBaseLoader returns by default; built by corpus/default_loader.py)."""
    rows = list(csv.DictReader(open(REPO / "corpus" / "manifest.csv")))
    if subset:
        keep = set(json.loads((REPO / "corpus" / subset).read_text()))
        rows = [r for r in rows if r["url"] in keep]
    docs = []
    for r in rows:
        rel = Path(r["file"]).relative_to("markdown")
        text = (REPO / "corpus" / variant / rel).read_text()
        docs.append({"text": text, "url": r["url"], "title": rel.stem})
    return docs


def load_questions(limit: int | None = None, file: str = "questions.jsonl") -> list[dict]:
    qs = [json.loads(l) for l in open(REPO / "questions" / file)]
    return qs[:limit] if limit else qs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("framework")
    ap.add_argument("--variant", default="clean")
    ap.add_argument("--subset", default=None, help="JSON list of URLs under corpus/")
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--reindex", action="store_true")
    ap.add_argument("--tag", default="")
    ap.add_argument("--questions", default="questions.jsonl")
    ap.add_argument("--start-run", type=int, default=1, help="number of the first run (for round-robin scheduling)")
    args = ap.parse_args()

    name = f"{args.framework}{args.tag}"
    out_dir = REPO / "results" / args.variant / name
    out_dir.mkdir(parents=True, exist_ok=True)
    os.environ["RAGBENCH_COLLECTION"] = f"{name}_{args.variant}".replace("-", "_")

    t0 = time.perf_counter()
    sys.path.insert(0, str(REPO / "pipelines" / args.framework))
    rag = importlib.import_module("rag")
    t_import = time.perf_counter() - t0

    t_index = None
    if args.reindex or not (out_dir / "index.json").exists():
        set_phase(f"index-{name}-{args.variant}")
        docs = load_docs(args.variant, args.subset)
        t1 = time.perf_counter()
        rag.build_index(docs)
        t_index = time.perf_counter() - t1
        (out_dir / "index.json").write_text(json.dumps({"docs": len(docs), "index_seconds": round(t_index, 2)}))

    questions = load_questions(args.limit, args.questions)
    for run in range(args.start_run, args.start_run + args.runs):
        set_phase(f"run-{name}-{args.variant}-r{run}")
        rows = []
        for q in questions:
            t2 = time.perf_counter()
            try:
                res = rag.answer(q["question"])
                err = None
            except Exception as e:  # keep going, record the failure
                res, err = {"answer": "", "contexts": []}, f"{type(e).__name__}: {e}"
            latency = time.perf_counter() - t2
            if err is None and res["answer"].strip() in ("", "Empty Response"):
                err = "EmptyAnswer: pipeline returned no answer without raising"
            rows.append({"id": q["id"], "question": q["question"], "answer": res["answer"],
                         "contexts": res["contexts"], "latency_s": round(latency, 3), "error": err})
        with open(out_dir / f"run{run}.jsonl", "w") as f:
            for r in rows:
                f.write(json.dumps(r) + "\n")
        lat = sorted(r["latency_s"] for r in rows)
        p = lambda q: lat[min(len(lat) - 1, int(q * len(lat)))]
        print(f"[{name}/{args.variant}] run {run}: {len(rows)} q, p50 {p(0.5):.2f}s, p95 {p(0.95):.2f}s, "
              f"errors {sum(1 for r in rows if r['error'])}")

    meta = {"import_seconds": round(t_import, 3), "first_answer_seconds": rows[0]["latency_s"] if rows else None}
    if t_index is not None:
        meta["index_seconds"] = round(t_index, 2)
    (out_dir / f"timing_r{args.start_run}.json").write_text(json.dumps(meta, indent=1))
    set_phase("idle")


if __name__ == "__main__":
    main()
