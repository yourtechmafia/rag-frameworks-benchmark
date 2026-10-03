"""Paired bootstrap: is a framework's Ragas score different from the baseline's?
Resamples the 100 questions 10,000 times; prints the mean difference and 95% CI.
Usage: python eval/significance.py [variant]"""
import csv
import random
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
variant = sys.argv[1] if len(sys.argv) > 1 else "clean"
METRICS = {"faithfulness": "faithfulness", "llm_context_precision_with_reference": "context precision",
           "context_recall": "context recall", "answer_correctness": "answer correctness"}


def load(fw):
    return {r["id"]: r for r in csv.DictReader(open(REPO / "results" / variant / fw / "ragas_run1.csv"))}


base = load("baseline")
random.seed(0)
print("| Framework | Metric | Diff vs plain Python | 95% CI | Real difference? |\n| --- | --- | --- | --- | --- |")
for fw in ["langchain", "llamaindex", "haystack", "dspy"]:
    other = load(fw)
    ids = sorted(set(base) & set(other))
    for col, name in METRICS.items():
        d = [float(other[i][col]) - float(base[i][col]) for i in ids]
        means = sorted(sum(random.choices(d, k=len(d))) / len(d) for _ in range(10000))
        lo, hi = means[250], means[9749]
        real = "yes" if lo > 0 or hi < 0 else "no"
        print(f"| {fw} | {name} | {sum(d) / len(d):+.3f} | [{lo:+.3f}, {hi:+.3f}] | {real} |")
