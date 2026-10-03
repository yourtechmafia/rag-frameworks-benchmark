"""Ingestion test table: retrieval by gold URL for each pipeline x corpus version.
Usage: python eval/ingestion_table.py"""
import importlib.util
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("retrieval", REPO / "eval" / "retrieval.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)
NAMES = {"default": "Default loader text", "markdown": "ScrapingBee markdown", "clean": "Cleaned markdown"}
print("| Pipeline | Corpus | hit@5 (all) | MRR (all) | hit@5 (JS-only, 28 q) | hit@5 (server-rendered, 72 q) |")
print("| --- | --- | --- | --- | --- | --- |")
for fw in ["baseline", "langchain", "llamaindex", "haystack"]:
    for v in ["default", "markdown", "clean"]:
        p = REPO / "results" / v / fw / "run1.jsonl"
        a, js, ssr = r.score(p), r.score(p, lambda q: q["js_only"]), r.score(p, lambda q: not q["js_only"])
        print(f"| {fw} | {NAMES[v]} | {a['hit@5']:.2f} | {a['mrr']:.2f} | {js['hit@5']:.2f} | {ssr['hit@5']:.2f} |")
