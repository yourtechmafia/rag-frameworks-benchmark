#!/usr/bin/env bash
# Install footprint: build a fresh venv from each pipeline's uv.lock, measure, delete.
set -euo pipefail
cd "$(dirname "$0")/.."
for fw in "$@"; do
  tmp=$(mktemp -d)
  (cd "pipelines/$fw" && UV_PROJECT_ENVIRONMENT="$tmp/venv" uv sync --frozen --no-install-project -q)
  n=$(VIRTUAL_ENV="$tmp/venv" uv pip list 2>/dev/null | tail -n +3 | wc -l | tr -d ' ')
  mb=$(( $(du -sk "$tmp/venv" | cut -f1) / 1024 ))
  echo "{\"framework\": \"$fw\", \"packages\": $n, \"size_mb\": $mb}"
  rm -rf "$tmp"
done
