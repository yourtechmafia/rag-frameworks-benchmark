#!/usr/bin/env bash
# Ingestion test: the same pipelines indexed from three versions of the corpus.
#   default  = BeautifulSoup get_text() of a plain GET (what WebBaseLoader returns)
#   markdown = ScrapingBee rendered markdown, as returned
#   clean    = markdown with nav/footers removed (reuses run 1 of the main benchmark)
set -uo pipefail
cd "$(dirname "$0")/.."
for v in default markdown; do
  for fw in baseline langchain llamaindex haystack; do
    scripts/run.sh "$fw" --variant "$v" --reindex 2>&1 | grep -E "^\["
  done
done
