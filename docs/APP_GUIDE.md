# LAST DICES // TERMINAL SCHOOL OS — App Usage Guide

## 1) First Run (Local, Kali-friendly)

```bash
bash scripts/bootstrap.sh
source .venv/bin/activate
python -m pytest
bash scripts/run_school.sh
```

Run watcher in another terminal:

```bash
source .venv/bin/activate
bash scripts/run_watcher.sh
```

## 2) How to Access Everything in the App

- Start screen/app shell: `bash scripts/run_school.sh`
- Navigate screens using app keybindings/menu (Dashboard, Curriculum, Lesson, Quiz, Assignments, Resources, Imports, Scanner, Agents, Settings).
- Generate a progress report with `r` in app.
- Quit app with `q`.

## 3) “Functional login” status

There is **no username/password login system** in this current scaffold.

Current behavior:
- single local learner profile persisted in SQLite
- profile defaults initialized in DB schema

If you want account-based login, that is a future feature (auth table + login screen + credential storage policy).

## 4) Where Study Data Lives

Runtime storage is local-first in `storage/`:
- DB: `storage/school.db`
- Imports inbox: `storage/import_materials/`
- Quarantine: `storage/quarantine/`
- Scan logs: `storage/logs/scans/`

## 5) How to Add Study Material Safely

1. Put files into:
   - `storage/import_materials/`
2. Let watcher process automatically (`bash scripts/run_watcher.sh`) or run manually:
   - `bash scripts/scan_imports.sh`
3. Scanner behavior:
   - clean => indexed
   - infected/suspicious => quarantined
   - scanner missing/failure => failed (safe default)

## 6) Recommended Daily Commands

```bash
source .venv/bin/activate
bash scripts/run_school.sh
bash scripts/run_watcher.sh
```

Optional checks:

```bash
python -m pytest
ruff check .
python -m last_dices_terminal_school.setup_seed
```

## 7) Common Issues

### App does not start
- Ensure venv active: `source .venv/bin/activate`
- Ensure package path includes `src` (scripts handle this)
- Re-run bootstrap: `bash scripts/bootstrap.sh`

### Imports not appearing
- Confirm watcher running
- Confirm files are in `storage/import_materials/`
- Check scan logs at `storage/logs/scans/scan.log`

### ClamAV missing
- System stays defensive and marks scans failed.
- Install if desired on Kali:
  - `sudo apt-get update && sudo apt-get install -y clamav`
