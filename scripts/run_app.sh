#!/usr/bin/env bash
set -euo pipefail

if [[ ! -d .venv ]]; then
  echo "[WARN] .venv missing. Run: bash scripts/bootstrap.sh"
fi

source .venv/bin/activate || true
export PYTHONPATH="${PYTHONPATH:-}:$(pwd)/src"

if ! command -v clamscan >/dev/null 2>&1; then
  echo "[WARN] clamscan missing; malware scan screen will show fallback states."
fi

python -m last_dices_terminal_school.main
