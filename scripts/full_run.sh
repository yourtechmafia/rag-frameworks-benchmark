#!/usr/bin/env bash
# Main benchmark: 5 pipelines x 3 runs x 100 questions on the cleaned corpus,
# scheduled round-robin so API latency drift is shared evenly.
set -uo pipefail
cd "$(dirname "$0")/.."
FWS="baseline langchain llamaindex haystack dspy"
for r in 1 2 3; do
  for fw in $FWS; do
    extra=""; [ "$r" = 1 ] && extra="--reindex"
    scripts/run.sh "$fw" --start-run "$r" $extra 2>&1 | grep -E "^\[" 
  done
done
