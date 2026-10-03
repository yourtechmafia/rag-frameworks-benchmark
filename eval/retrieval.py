"""Retrieval metrics that need no LLM: did a gold page appear in the top-k chunks?

hit@k  = share of questions where at least one retrieved chunk comes from a gold URL
recall = share of a question's gold URLs that appear among the retrieved chunks (averaged)
MRR    = mean reciprocal rank of the first chunk from a gold URL

Usage: python eval/retrieval.py results/clean/langchain/run1.jsonl [more files...]
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
GOLD = {q["id"]: q for q in map(json.loads, open(REPO / "questions" / "questions.jsonl"))}


def score(path: Path, subset=None) -> dict:
    rows = [json.loads(l) for l in open(path)]
    if subset:
        rows = [r for r in rows if subset(GOLD[r["id"]])]
    hits = rr = rec = 0.0
    for r in rows:
        gold = set(GOLD[r["id"]]["gold_urls"])
        urls = [c["url"] for c in r["contexts"]]
        ranks = [i for i, u in enumerate(urls, 1) if u in gold]
        hits += bool(ranks)
        rr += 1 / ranks[0] if ranks else 0
        rec += len(gold & set(urls)) / len(gold)
    n = len(rows) or 1
    return {"n": len(rows), "hit@5": round(hits / n, 3), "gold_recall@5": round(rec / n, 3), "mrr": round(rr / n, 3)}


if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(p, score(Path(p)))
