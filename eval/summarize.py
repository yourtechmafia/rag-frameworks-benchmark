"""Build the results tables from raw outputs (results/, ledger/spend.csv).

Writes results/summary.csv and results/summary.md. Standard library only.
Usage: python eval/summarize.py [--variant clean] [--frameworks baseline,langchain,...]
"""
import argparse
import csv
import json
import statistics as st
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
GOLD = {q["id"]: q for q in map(json.loads, open(REPO / "questions" / "questions.jsonl"))}
RAGAS_COLS = {"faithfulness": "faithfulness", "llm_context_precision_with_reference": "context_precision",
              "context_recall": "context_recall", "answer_correctness": "answer_correctness"}


def pct(values, q):
    v = sorted(values)
    return v[min(len(v) - 1, int(round(q * (len(v) - 1))))]


def ledger_by_phase():
    agg = defaultdict(lambda: {"calls": 0, "in": 0, "out": 0, "usd": 0.0})
    for r in csv.DictReader(open(REPO / "ledger" / "spend.csv")):
        a = agg[r["phase"]]
        a["calls"] += 1
        a["in"] += int(r["input_tokens"] or 0)
        a["out"] += int(r["output_tokens"] or 0)
        a["usd"] += float(r["cost_usd"] or 0)
    return agg


def retrieval(rows):
    hits = rr = 0.0
    for r in rows:
        gold = set(GOLD[r["id"]]["gold_urls"])
        ranks = [i for i, c in enumerate(r["contexts"], 1) if c["url"] in gold]
        hits += bool(ranks)
        rr += 1 / ranks[0] if ranks else 0
    return hits / len(rows), rr / len(rows)


def ragas_means(path, subset=None):
    if not path.exists():
        return {}
    rows = list(csv.DictReader(open(path)))
    if subset:
        rows = [r for r in rows if subset(GOLD[r["id"]])]
    out = {}
    for src, name in RAGAS_COLS.items():
        vals = [float(r[src]) for r in rows if r.get(src) not in (None, "", "nan")]
        out[name] = round(st.mean(vals), 3) if vals else None
    return out


def summarize(fw, variant, ledger):
    d = REPO / "results" / variant / fw
    runs = {}
    for p in sorted(d.glob("run*.jsonl")):
        runs[int(p.stem[3:])] = [json.loads(l) for l in open(p)]
    if not runs:
        return None
    lat = [r["latency_s"] for rows in runs.values() for r in rows if not r["error"]]
    errors = sum(1 for rows in runs.values() for r in rows if r["error"])
    # Answer stability: share of questions with byte-identical answers in every run.
    ids = [r["id"] for r in runs[min(runs)]]
    answers = {i: {rows_by_id[i]["answer"] for rows_by_id in ({r["id"]: r for r in rows} for rows in runs.values())}
               for i in ids}
    stable = sum(1 for a in answers.values() if len(a) == 1) / len(ids)
    hit, mrr = retrieval(runs[min(runs)])
    phases = [ledger.get(f"run-{fw}-{variant}-r{k}") for k in runs]
    phases = [p for p in phases if p]
    calls = sum(p["calls"] for p in phases)
    n_q = sum(len(rows) for rows in runs.values())
    timing = [json.loads(p.read_text()) for p in d.glob("timing_r*.json")]
    index = json.loads((d / "index.json").read_text()) if (d / "index.json").exists() else {}
    row = {
        "framework": fw, "variant": variant, "runs": len(runs), "questions": len(ids), "errors": errors,
        "p50_s": round(pct(lat, 0.5), 2), "p95_s": round(pct(lat, 0.95), 2),
        "mean_s": round(st.mean(lat), 2),
        "llm_calls_per_q": round(calls / n_q, 2) if n_q else None,
        "in_tokens_per_q": round(sum(p["in"] for p in phases) / n_q) if n_q else None,
        "out_tokens_per_q": round(sum(p["out"] for p in phases) / n_q) if n_q else None,
        "usd_per_100q": round(100 * sum(p["usd"] for p in phases) / n_q, 3) if n_q else None,
        "index_s": index.get("index_seconds"),
        "import_s": round(st.median(t["import_seconds"] for t in timing), 2) if timing else None,
        "first_answer_s": round(st.median(t["first_answer_seconds"] for t in timing), 2) if timing else None,
        "hit@5": round(hit, 3), "mrr": round(mrr, 3), "answer_stability": round(stable, 3),
    }
    row.update(ragas_means(d / "ragas_run1.csv"))
    row["answer_correctness_js_only"] = ragas_means(d / "ragas_run1.csv", lambda q: q["js_only"]).get("answer_correctness")
    row["answer_correctness_multi_hop"] = ragas_means(d / "ragas_run1.csv", lambda q: q["hop"] == "multi").get("answer_correctness")
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", default="clean")
    ap.add_argument("--frameworks", default="baseline,langchain,llamaindex,haystack,dspy")
    ap.add_argument("--out", default="summary")
    args = ap.parse_args()
    ledger = ledger_by_phase()
    rows = [r for fw in args.frameworks.split(",") if (r := summarize(fw, args.variant, ledger))]
    cols = list(rows[0].keys())
    for r in rows:
        cols += [k for k in r if k not in cols]
    with open(REPO / "results" / f"{args.out}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    md = ["| " + " | ".join(cols) + " |", "|" + " --- |" * len(cols)]
    md += ["| " + " | ".join(str(r.get(c, "")) for c in cols) + " |" for r in rows]
    (REPO / "results" / f"{args.out}.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
