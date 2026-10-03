#!/usr/bin/env bash
# Run one framework through the harness inside its own venv, routed through the
# spend-ledger proxy on :8788. Usage: scripts/run.sh <framework> [harness args...]
set -euo pipefail
FW=$1; shift
cd "$(dirname "$0")/.."
export ANTHROPIC_BASE_URL=http://127.0.0.1:8788
export BENCH_PHASE_FILE=$HOME/ragbench/phase_pipe.txt
export HF_HUB_OFFLINE=1 TOKENIZERS_PARALLELISM=false
export PYTHONPATH="$PWD/pipelines"
exec "$HOME/ragbench/envs/$FW/bin/python" pipelines/harness.py "$FW" "$@"
