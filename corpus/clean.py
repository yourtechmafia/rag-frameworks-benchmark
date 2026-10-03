"""Turn ScrapingBee markdown into cleaned markdown (corpus/clean/).

The rules are generic, not tuned per page:
  * drop everything above the page's first real H1 (site nav, search box)
  * drop images, heading permalinks ([#](#x)) and link wrappers around headings
  * drop footer lines (Back to top, Powered by, Edit page, last-updated dates)
  * collapse runs of blank lines
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).parent

H1_UNDERLINE = re.compile(r"^=+\s*$")
ROOT_LINK = re.compile(r"^\[[^\]]+\]\((/[\w-]*/?|#/?)\)\s*$")  # [site](/site/) or [site](#/)
IMAGE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
PERMALINK = re.compile(r"\[#\]\(#[^)]*\)")
HEADING_LINK = re.compile(r"^(#{1,6}\s+)?\[([^\]]+)\]\(#[^)]*\)\s*$")
FOOTER = re.compile(
    r"^(Back to top|Powered by .*|.*Edit (this )?[Pp]age.*|"
    r"(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4})\s*$"
)


def h1_positions(lines):
    for i, line in enumerate(lines):
        if line.startswith("# "):
            yield i, line[2:].strip()
        elif i > 0 and H1_UNDERLINE.match(line) and lines[i - 1].strip():
            yield i - 1, lines[i - 1].strip()


def clean(text: str) -> str:
    lines = text.splitlines()
    start = 0
    for i, title in h1_positions(lines):
        if ROOT_LINK.match(title):
            start = i + 2  # skip the site header, keep looking for the page H1
            continue
        start = i
        break
    out = []
    for line in lines[start:]:
        if FOOTER.match(line.strip()):
            continue
        line = IMAGE.sub("", PERMALINK.sub("", line))
        m = HEADING_LINK.match(line)
        if m:
            line = (m.group(1) or "") + m.group(2)
        out.append(line.rstrip())
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


def main() -> None:
    rows = list(csv.DictReader(open(ROOT / "manifest.csv")))
    before = after = 0
    for r in rows:
        src = ROOT / r["file"]
        dst = ROOT / "clean" / Path(r["file"]).relative_to("markdown")
        dst.parent.mkdir(parents=True, exist_ok=True)
        text = src.read_text()
        cleaned = clean(text)
        dst.write_text(cleaned)
        before += len(text)
        after += len(cleaned)
    print(f"{len(rows)} pages: {before:,} -> {after:,} chars ({1 - after / before:.0%} removed)")


if __name__ == "__main__":
    main()
