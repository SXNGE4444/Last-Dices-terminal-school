#!/usr/bin/env bash
set -euo pipefail

printf "[LAST DICES] Bootstrap starting...\n"

if ! command -v python3 >/dev/null 2>&1; then
  echo "[ERR] python3 is required." >&2
  exit 1
fi

PY_VER=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
if [[ "$PY_VER" < "3.11" ]]; then
  echo "[ERR] Python 3.11+ required. Found: $PY_VER" >&2
  exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt || {
  echo "[WARN] Dependency installation incomplete (likely network/proxy issue)."
  echo "[WARN] You can still inspect code and run compile checks."
}

mkdir -p storage/import_materials storage/quarantine storage/logs storage/logs/scans
mkdir -p import_materials quarantine logs logs/scans

if command -v clamscan >/dev/null 2>&1; then
  echo "[OK] ClamAV scanner detected."
else
  echo "[WARN] clamscan not found. Import scanner will use safe fallback status=failed."
  echo "[WARN] Install on Kali: sudo apt-get update && sudo apt-get install -y clamav"
fi

export PYTHONPATH="${PYTHONPATH:-}:$(pwd)/src"
export LDTS_REPO_ROOT="$(pwd)"
export LDTS_STORAGE_ROOT="$(pwd)/storage"

python -m last_dices_terminal_school.setup_seed || echo "[WARN] Seed setup skipped due to missing Python deps."

echo "[OK] Bootstrap complete. Run: bash scripts/run_app.sh"
