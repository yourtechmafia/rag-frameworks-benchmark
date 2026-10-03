"""Bar charts for the article: lines of code, p95 latency, answer correctness.

Reads results/summary_main.csv and results/loc.json; writes PNGs to
results/charts/. Every chart's numbers are also printed as a markdown table.
"""
import csv
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "results" / "charts"
OUT.mkdir(parents=True, exist_ok=True)
NAMES = {"baseline": "Plain Python", "langchain": "LangChain", "llamaindex": "LlamaIndex",
         "haystack": "Haystack", "dspy": "DSPy"}
HONEY, INK, GRID = "#F5B70A", "#1D1D1F", "#E6E6E6"

plt.rcParams.update({"font.family": "Helvetica", "font.size": 13, "axes.edgecolor": GRID,
                     "axes.spines.top": False, "axes.spines.right": False})

rows = {r["framework"]: r for r in csv.DictReader(open(REPO / "results" / "summary_main.csv"))}
loc = json.loads((REPO / "results" / "loc.json").read_text())


def bar(metric_name, values, fmt, filename, title, note, lower_is_better):
    items = sorted(values.items(), key=lambda kv: kv[1], reverse=not lower_is_better)
    labels = [NAMES[k] for k, _ in items]
    nums = [v for _, v in items]
    fig, ax = plt.subplots(figsize=(9, 4.6), dpi=200)
    colors = [INK if k == "baseline" else HONEY for k, _ in items]
    bars = ax.barh(labels[::-1], nums[::-1], color=colors[::-1], height=0.6)
    for b, v in zip(bars, nums[::-1]):
        ax.text(b.get_width(), b.get_y() + b.get_height() / 2, " " + fmt.format(v), va="center", fontsize=12)
    ax.set_title(title, loc="left", fontsize=15, fontweight="bold", pad=14)
    ax.set_xlabel(f"{metric_name} ({note})", fontsize=11, color="#555")
    ax.xaxis.grid(True, color=GRID)
    ax.set_axisbelow(True)
    ax.set_xlim(0, max(nums) * 1.18)
    fig.text(0.01, 0.01, "Same corpus, model and settings for every pipeline. October 3, 2026.", fontsize=9, color="#777")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(OUT / filename)
    plt.close(fig)
    print(f"\n{title}\n\n| Pipeline | {metric_name} |\n| --- | --- |")
    for k, v in items:
        print(f"| {NAMES[k]} | {fmt.format(v)} |")


bar("Lines of code", {k: loc[k] for k in NAMES}, "{:d}", "loc.png",
    "Lines of code for ingestion and querying", "pygount, lower is less code", True)
bar("p95 latency", {k: float(rows[k]["p95_s"]) for k in NAMES}, "{:.2f} s", "p95_latency.png",
    "p95 query latency over 300 queries", "seconds, lower is faster", True)
if "answer_correctness" in next(iter(rows.values())):
    bar("Answer correctness", {k: float(rows[k]["answer_correctness"]) for k in NAMES}, "{:.3f}",
        "answer_correctness.png", "Ragas answer correctness, 100 questions", "0 to 1, higher is better", False)
