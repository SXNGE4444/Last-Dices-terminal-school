#!/usr/bin/env bash
set -euo pipefail

source .venv/bin/activate
export PYTHONPATH="${PYTHONPATH:-}:$(pwd)/src"
python -m last_dices_terminal_school.import_cli
