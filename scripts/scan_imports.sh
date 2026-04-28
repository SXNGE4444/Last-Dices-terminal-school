#!/usr/bin/env bash
set -euo pipefail

source .venv/bin/activate
export PYTHONPATH="${PYTHONPATH:-}:$(pwd)/src"
export LDTS_REPO_ROOT="$(pwd)"
export LDTS_STORAGE_ROOT="$(pwd)/storage"

python -m last_dices_terminal_school.import_cli
