#!/usr/bin/env bash
# Graph RAG on the 100-page subset (corpus/subset_graph.json), 40 questions
# (questions/graph_subset.jsonl), one run each, plus the baseline on the same
# subset for comparison. Uses its own logging proxy (:8789) and phase file.
# GraphRAG also needs scripts/embed_server.py listening on :8790.
set -uo pipefail
cd "$(dirname "$0")/.."
export ANTHROPIC_BASE_URL=http://127.0.0.1:8789 BENCH_PHASE_FILE=$HOME/ragbench/phase_graph.txt
export HF_HUB_OFFLINE=1 TOKENIZERS_PARALLELISM=false PYTHONPATH="$PWD/pipelines"
Q="--questions graph_subset.jsonl --subset subset_graph.json --reindex --tag=-subset"
for fw in baseline lightrag graphrag; do
  "$HOME/ragbench/envs/$fw/bin/python" pipelines/harness.py "$fw" $Q 2>&1 | grep -E "^\[|Traceback|Error:" | tail -3
done
