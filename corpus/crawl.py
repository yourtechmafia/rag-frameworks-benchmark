"""Crawl and freeze the benchmark corpus.

For every URL in corpus/urls.csv this script stores two things:
  1. raw/<site>/<slug>.html  -- a plain HTTP GET, what a default loader sees
  2. markdown/<site>/<slug>.md -- ScrapingBee's markdown output

Server-rendered sites use render_js=false (1 credit). Client-rendered sites
use render_js=true plus a wait_for selector (5 credits).

Usage:
  export SCRAPINGBEE_API_KEY=...
  python corpus/crawl.py            # skips pages already on disk
"""
import csv
import hashlib
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).parent
API = "https://app.scrapingbee.com/api/v1/"
HEADERS = {"Authorization": f"Bearer {os.environ['SCRAPINGBEE_API_KEY']}"}
UA = {"User-Agent": "Mozilla/5.0 (rag-frameworks-benchmark)"}

SITES = {
    "uv": {"render_js": False},
    "pnpm": {"render_js": False},
    "go-echarts": {"render_js": True, "wait_for": ".markdown-section > *"},
    "docsify": {"render_js": True, "wait_for": ".markdown-section > *"},
}


def slug(url: str) -> str:
    s = re.sub(r"^https?://[^/]+/", "", url).replace("#/", "")
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")
    return s or "index"


def fetch(row: dict) -> dict:
    site, url = row["site"], row["url"]
    name = slug(url)
    md_path = ROOT / "markdown" / site / f"{name}.md"
    raw_path = ROOT / "raw" / site / f"{name}.html"
    md_path.parent.mkdir(parents=True, exist_ok=True)
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path = md_path.with_suffix(".json")
    if meta_path.exists():
        return json.loads(meta_path.read_text())

    # 1. What a default loader gets: one plain GET, no JavaScript.
    raw = requests.get(url, headers=UA, timeout=30)
    raw_path.write_text(raw.text)

    # 2. ScrapingBee markdown, rendering JavaScript only where the site needs it.
    cfg = SITES[site]
    params = {
        "url": url,
        "render_js": str(cfg["render_js"]).lower(),
        "return_page_markdown": "true",
    }
    if cfg.get("wait_for"):
        params["wait_for"] = cfg["wait_for"]
    for attempt in range(3):
        t0 = time.time()
        r = requests.get(API, params=params, headers=HEADERS, timeout=150)
        if r.status_code == 200 and len(r.text) > 200:
            break
        time.sleep(3 * (attempt + 1))
    md_path.write_text(r.text)

    meta = {
        "site": site,
        "url": url,
        "file": f"markdown/{site}/{name}.md",
        "render_js": cfg["render_js"],
        "status": r.status_code,
        "credits": int(r.headers.get("Spb-cost", 0) or 0),
        "seconds": round(time.time() - t0, 2),
        "markdown_chars": len(r.text),
        "raw_html_chars": len(raw.text),
        "sha256": hashlib.sha256(r.text.encode()).hexdigest(),
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    meta_path.write_text(json.dumps(meta, indent=1))
    return meta


def main() -> None:
    rows = list(csv.DictReader(open(ROOT / "urls.csv")))
    with ThreadPoolExecutor(max_workers=5) as pool:
        results = list(pool.map(fetch, rows))
    with open(ROOT / "manifest.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        w.writeheader()
        w.writerows(results)
    bad = [m for m in results if m["status"] != 200 or m["markdown_chars"] < 200]
    print(f"{len(results)} pages, {sum(m['credits'] for m in results)} credits, {len(bad)} suspect")
    for m in bad:
        print("  suspect:", m["status"], m["markdown_chars"], m["url"], file=sys.stderr)


if __name__ == "__main__":
    main()
