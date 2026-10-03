"""Build corpus/default/: the text a default HTML loader extracts from each page.

LangChain's WebBaseLoader fetches the URL with requests and returns
BeautifulSoup(html, "html.parser").get_text(). We apply the same call to the
plain-GET HTML frozen in corpus/raw/, so the 'default' variant is reproducible.
"""
import csv
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).parent

for r in csv.DictReader(open(ROOT / "manifest.csv")):
    rel = Path(r["file"]).relative_to("markdown")
    html = (ROOT / "raw" / rel.with_suffix(".html")).read_text()
    out = ROOT / "default" / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(BeautifulSoup(html, "html.parser").get_text())
