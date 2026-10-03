"""Summarize the spend ledger by phase."""
import csv, sys
from collections import defaultdict
from pathlib import Path

ledger = Path(__file__).resolve().parents[1] / "ledger" / "spend.csv"
rows = list(csv.DictReader(ledger.open())) if ledger.exists() else []
by = defaultdict(lambda: [0, 0, 0, 0, 0.0])
for r in rows:
    b = by[r["phase"]]
    b[0] += 1; b[1] += int(r["input_tokens"]); b[2] += int(r["output_tokens"])
    b[3] += int(r["cache_read_input_tokens"]); b[4] += float(r["cost_usd"])
print(f"{'phase':28s} {'calls':>6s} {'in_tok':>10s} {'out_tok':>9s} {'cache_rd':>9s} {'usd':>8s}")
for p, (n, i, o, c, usd) in sorted(by.items()):
    print(f"{p:28s} {n:6d} {i:10d} {o:9d} {c:9d} {usd:8.4f}")
print(f"{'TOTAL':28s} {sum(b[0] for b in by.values()):6d} {'':10s} {'':9s} {'':9s} {sum(b[4] for b in by.values()):8.4f}")
