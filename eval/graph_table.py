"""Graph RAG subset table (100 pages, 40 questions): plain Python vs LightRAG vs GraphRAG.
Usage: python eval/graph_table.py"""
import csv
import json
import random
import statistics as st
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ledger = list(csv.DictReader(open(REPO / "ledger" / "spend.csv")))


def cost(phase):
    rows = [r for r in ledger if r["phase"] == phase]
    return len(rows), sum(float(r["cost_usd"]) for r in rows), sum(int(r["input_tokens"]) for r in rows)


def ragas(fw):
    return {r["id"]: r for r in csv.DictReader(open(REPO / f"results/clean/{fw}-subset/ragas_run1.csv"))}


def mean(rows, col):
    v = [float(r[col]) for r in rows.values() if r[col] not in ("", "nan")]
    return (st.mean(v), len(v)) if v else (None, 0)


base = ragas("baseline")
print("| Pipeline | Indexing cost | Index LLM calls | Query p50 / p95 | Input tokens per query | Answer correctness | Faithfulness | Context recall | Context precision |")
print("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
for fw in ("baseline", "lightrag", "graphrag"):
    n_idx, usd_idx, _ = cost(f"index-{fw}-subset-clean")
    n_q, _, tok_q = cost(f"run-{fw}-subset-clean-r1")
    lat = sorted(json.loads(l)["latency_s"] for l in open(REPO / f"results/clean/{fw}-subset/run1.jsonl"))
    r = ragas(fw)
    cells = []
    for col in ("answer_correctness", "faithfulness", "context_recall", "llm_context_precision_with_reference"):
        m, n = mean(r, col)
        cells.append(f"{m:.3f}" if n >= 30 else f"n/a ({n} of 40 scored)")
    print(f"| {fw} | ${usd_idx:.2f} | {n_idx} | {lat[len(lat) // 2]:.2f} s / {lat[int(0.95 * (len(lat) - 1))]:.2f} s | "
          f"{tok_q / 40:,.0f} | " + " | ".join(cells) + " |")
random.seed(0)
print()
for fw in ("lightrag", "graphrag"):
    r = ragas(fw)
    for col in ("answer_correctness", "faithfulness", "context_recall"):
        d = [float(r[i][col]) - float(base[i][col]) for i in base]
        ms = sorted(sum(random.choices(d, k=len(d))) / len(d) for _ in range(10000))
        print(f"{fw} {col} vs plain Python: {st.mean(d):+.3f} (95% CI {ms[250]:+.3f} to {ms[9749]:+.3f})")
