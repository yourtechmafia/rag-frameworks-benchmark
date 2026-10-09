"""Charts for the article's results section, built from the result files.

1. results_comparison.png: six small-multiple bar panels, one per metric.
2. results_ingestion.png: answer correctness by corpus version, plus
   JavaScript-only retrieval hit@5 across four pipelines.

Usage: python eval/charts_results.py [output_dir]   (default results/charts)
"""
import csv
import importlib.util
import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

REPO = Path(__file__).resolve().parents[1]
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "results" / "charts"
OUT.mkdir(parents=True, exist_ok=True)

SURFACE, INK, INK2, MUTED, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#8a8984", "#e8e7e3"
BLUE, ORANGE = "#2a78d6", "#eb6834"  # validated pair (light surface)
ORDER = ["baseline", "langchain", "llamaindex", "haystack", "dspy"]
NAMES = {"baseline": "Plain Python", "langchain": "LangChain", "llamaindex": "LlamaIndex",
         "haystack": "Haystack", "dspy": "DSPy"}
plt.rcParams.update({"font.family": "Helvetica", "font.size": 12, "text.color": INK,
                     "axes.edgecolor": GRID, "axes.labelcolor": INK2,
                     "xtick.color": MUTED, "ytick.color": INK, "figure.facecolor": SURFACE,
                     "axes.facecolor": SURFACE})


def rounded_barh(ax, y, width, height, color):
    """Horizontal bar anchored at zero, with a softly rounded data end."""
    ax.add_patch(FancyBboxPatch((0, y - height / 2), width, height, mutation_aspect=0.02,
                                boxstyle="round,pad=0,rounding_size=0.004", linewidth=0, facecolor=color))


def style(ax):
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.xaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", length=0, labelsize=10)


def footer(fig, text):
    fig.text(0.012, 0.012, text, fontsize=9, color=MUTED, ha="left", va="bottom")


# ---------- 1. comparison small multiples ----------
rows = {r["framework"]: r for r in csv.DictReader(open(REPO / "results" / "summary_main.csv"))}
loc = json.loads((REPO / "results" / "loc.json").read_text())
panels = [
    ("Lines of code", "lower is less code", {k: loc[k] for k in ORDER}, "{:.0f}"),
    ("p50 latency (s)", "lower is faster", {k: float(rows[k]["p50_s"]) for k in ORDER}, "{:.2f}"),
    ("p95 latency (s)", "lower is faster", {k: float(rows[k]["p95_s"]) for k in ORDER}, "{:.2f}"),
    ("Cost per 100 questions ($)", "lower is cheaper", {k: float(rows[k]["usd_per_100q"]) for k in ORDER}, "{:.3f}"),
    ("Answer correctness", "0 to 1, higher is better", {k: float(rows[k]["answer_correctness"]) for k in ORDER}, "{:.3f}"),
    ("Context precision", "0 to 1, higher is better", {k: float(rows[k]["context_precision"]) for k in ORDER}, "{:.3f}"),
]
fig, axes = plt.subplots(2, 3, figsize=(13, 7.2), dpi=200)
ys = list(range(len(ORDER)))[::-1]
for ax, (title, note, vals, fmt) in zip(axes.flat, panels):
    top = max(vals.values()) * 1.32
    for y, k in zip(ys, ORDER):
        rounded_barh(ax, y, vals[k], 0.56, INK2 if k == "baseline" else BLUE)
        ax.text(vals[k] + top * 0.015, y, fmt.format(vals[k]), va="center", fontsize=10.5, color=INK)
    ax.set_xlim(0, top)
    ax.set_ylim(-0.6, len(ORDER) - 0.4)
    ax.set_yticks(ys)
    ax.set_yticklabels([NAMES[k] for k in ORDER], fontsize=11)
    ax.set_title(title, loc="left", fontsize=13, fontweight="bold", pad=20)
    ax.text(0, 1.015, note, transform=ax.transAxes, fontsize=9.5, color=MUTED, va="bottom", ha="left")
    style(ax)
    if ax not in axes[:, 0]:
        ax.set_yticklabels([])
fig.suptitle("Five RAG pipelines on the same 310 pages, questions and model", x=0.012, ha="left",
             fontsize=16, fontweight="bold", y=0.985)
fig.text(0.012, 0.935, "Plain Python baseline in dark grey. Latency over 300 queries; Ragas scores on run 1, judged by Claude Haiku 4.5.",
         fontsize=10.5, color=INK2, ha="left")
footer(fig, "Benchmark run October 3, 2026. Data and code: github.com/yourtechmafia/rag-frameworks-benchmark")
fig.tight_layout(rect=(0, 0.03, 1, 0.94), h_pad=2.2, w_pad=1.5)
fig.savefig(OUT / "results_comparison.png", facecolor=SURFACE)
plt.close(fig)

# ---------- 2. ingestion ----------
gold = {q["id"]: q for q in map(json.loads, open(REPO / "questions" / "questions.jsonl"))}
VARIANTS = [("default", "Default loader text"), ("markdown", "ScrapingBee markdown"), ("clean", "Cleaned markdown")]


def ac(variant, subset):
    rs = [r for r in csv.DictReader(open(REPO / f"results/{variant}/baseline/ragas_run1.csv")) if subset(gold[r["id"]])]
    return sum(float(r["answer_correctness"]) for r in rs) / len(rs)


spec = importlib.util.spec_from_file_location("retrieval", REPO / "eval" / "retrieval.py")
retrieval = importlib.util.module_from_spec(spec)
spec.loader.exec_module(retrieval)
hit = {v: [retrieval.score(REPO / f"results/{v}/{fw}/run1.jsonl", lambda q: q["js_only"])["hit@5"]
           for fw in ("baseline", "langchain", "llamaindex", "haystack")] for v, _ in VARIANTS}

fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 5.6), dpi=200, gridspec_kw={"width_ratios": [1.45, 1]})
labels = [n for _, n in VARIANTS]
ys = [2, 1, 0]
h = 0.34
for y, (v, _) in zip(ys, VARIANTS):
    for off, color, val in ((h / 2 + 0.02, BLUE, ac(v, lambda q: True)), (-h / 2 - 0.02, ORANGE, ac(v, lambda q: q["js_only"]))):
        rounded_barh(a1, y + off, val, h, color)
        a1.text(val + 0.012, y + off, f"{val:.3f}", va="center", fontsize=10.5)
a1.set_xlim(0, 0.82)
a1.set_ylim(-0.6, 2.6)
a1.set_yticks(ys)
a1.set_yticklabels(labels, fontsize=11.5)
a1.set_title("Answer correctness, plain Python pipeline", loc="left", fontsize=13, fontweight="bold", pad=22)
a1.text(0, 1.015, "0 to 1, higher is better", transform=a1.transAxes, fontsize=9.5, color=MUTED, va="bottom")
fig.legend(handles=[plt.Rectangle((0, 0), 1, 1, color=BLUE), plt.Rectangle((0, 0), 1, 1, color=ORANGE)],
           labels=["All 100 questions", "28 JavaScript-only questions"], loc="upper left",
           bbox_to_anchor=(0.006, 0.935), ncol=2, frameon=False, fontsize=10.5, handlelength=1.2)
style(a1)

for y, (v, _) in zip(ys, VARIANTS):
    lo, hi = min(hit[v]), max(hit[v])
    a2.plot([lo, hi], [y, y], color=ORANGE, alpha=0.35, linewidth=8, solid_capstyle="round", zorder=2)
    a2.scatter(hit[v], [y] * len(hit[v]), s=46, color=ORANGE, edgecolor=SURFACE, linewidth=1.5, zorder=3)
    a2.text(hi + 0.03, y, f"{lo:.2f} to {hi:.2f}", va="center", fontsize=10.5)
a2.set_xlim(0, 1.2)
a2.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
a2.set_ylim(-0.6, 2.6)
a2.set_yticks(ys)
a2.set_yticklabels([])
a2.set_title("Gold page in the top 5, JavaScript-only", loc="left", fontsize=13, fontweight="bold", pad=22)
a2.text(0, 1.015, "Retrieval hit@5; one dot per pipeline (LangChain, LlamaIndex, Haystack, plain Python)",
        transform=a2.transAxes, fontsize=9.5, color=MUTED, va="bottom")
style(a2)
fig.suptitle("Rendering the pages mattered more than the framework", x=0.012, ha="left", fontsize=16,
             fontweight="bold", y=0.985)
footer(fig, "Same questions and settings for every corpus version. Benchmark run October 3, 2026. Data: github.com/yourtechmafia/rag-frameworks-benchmark")
fig.tight_layout(rect=(0, 0.04, 1, 0.9), w_pad=3)
fig.savefig(OUT / "results_ingestion.png", facecolor=SURFACE)
plt.close(fig)
print("wrote", OUT / "results_comparison.png", "and", OUT / "results_ingestion.png")
