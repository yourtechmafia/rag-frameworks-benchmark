"""Framework overhead outside the LLM call: pipeline latency minus the API
latency the logging proxy recorded for the same request (runs 1-3, clean corpus).
Usage: python eval/overhead.py"""
import csv
import json
import statistics as st
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ledger = list(csv.DictReader(open(REPO / "ledger" / "spend.csv")))
print("| Framework | Mean latency | Mean API time | Overhead median | Overhead p95 |\n| --- | --- | --- | --- | --- |")
for fw in ["baseline", "langchain", "llamaindex", "haystack", "dspy"]:
    total, api = [], []
    for r in (1, 2, 3):
        rows = [json.loads(l) for l in open(REPO / f"results/clean/{fw}/run{r}.jsonl")]
        calls = [float(x["latency_ms"]) / 1000 for x in ledger if x["phase"] == f"run-{fw}-clean-r{r}"]
        assert len(calls) == len(rows), f"{fw} run {r}: {len(calls)} calls vs {len(rows)} answers"
        total += [x["latency_s"] for x in rows]
        api += calls
    over = sorted(t - a for t, a in zip(total, api))
    print(f"| {fw} | {st.mean(total):.2f} s | {st.mean(api):.2f} s | {st.median(over) * 1000:.0f} ms | "
          f"{over[int(0.95 * len(over))] * 1000:.0f} ms |")
