"""Ragas scores for the baseline pipeline on each corpus version, by question type,
plus paired-bootstrap CIs. Usage: python eval/ingestion_quality.py"""
import csv
import json
import random
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
gold = {q["id"]: q for q in map(json.loads, open(REPO / "questions" / "questions.jsonl"))}
runs = {v: {r["id"]: r for r in csv.DictReader(open(REPO / f"results/{v}/baseline/ragas_run1.csv"))}
        for v in ("default", "markdown", "clean")}
subsets = {"All 100": lambda q: True, "JS-only (28)": lambda q: q["js_only"],
           "Server-rendered (72)": lambda q: not q["js_only"]}
print("| Questions | Metric | Default loader text | ScrapingBee markdown | Cleaned markdown |\n| --- | --- | --- | --- | --- |")
for name, f in subsets.items():
    ids = [i for i in runs["clean"] if f(gold[i])]
    for col in ("answer_correctness", "context_recall"):
        vals = [sum(float(runs[v][i][col]) for i in ids) / len(ids) for v in ("default", "markdown", "clean")]
        print(f"| {name} | {col.replace('_', ' ')} | " + " | ".join(f"{x:.3f}" for x in vals) + " |")
random.seed(0)
print()
for a, b in (("default", "clean"), ("markdown", "clean")):
    d = [float(runs[b][i]["answer_correctness"]) - float(runs[a][i]["answer_correctness"]) for i in runs[b]]
    ms = sorted(sum(random.choices(d, k=len(d))) / len(d) for _ in range(10000))
    print(f"Answer correctness, {b} minus {a}: {sum(d) / len(d):+.3f} (95% CI {ms[250]:+.3f} to {ms[9749]:+.3f})")
