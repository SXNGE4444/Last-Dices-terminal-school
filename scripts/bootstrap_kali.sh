#!/usr/bin/env bash
set -euo pipefail

printf "[LAST DICES] Bootstrapping local environment...\n"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required." >&2
  exit 1
fi

PY_VER=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
if [[ "$PY_VER" < "3.11" ]]; then
  echo "Python 3.11+ required. Found: $PY_VER" >&2
  exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

if command -v apt-get >/dev/null 2>&1; then
  echo "[LAST DICES] Optional: install clamav if missing"
  if ! command -v clamscan >/dev/null 2>&1; then
    echo "Run manually if desired: sudo apt-get update && sudo apt-get install -y clamav"
  fi
fi

mkdir -p storage/import_materials storage/quarantine storage/logs storage/logs/scans
mkdir -p import_materials quarantine logs logs/scans
printf "[LAST DICES] Bootstrap complete.\n"
printf "[LAST DICES] Run app: bash scripts/run_school.sh\n"
printf "[LAST DICES] Run watcher: bash scripts/run_watcher.sh\n"
