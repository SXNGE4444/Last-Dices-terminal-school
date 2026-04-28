# LAST DICES // TERMINAL SCHOOL OS — Master Scope (Pre-Implementation)

> This document defines structure and scope before additional coding work.

## 1) Full GitHub-Ready Repository Structure

```text
.
├── README.md
├── pyproject.toml
├── requirements.txt
├── Makefile
├── .gitignore
├── .env.example
├── data/
│   ├── curriculum/
│   │   ├── manifest.yaml
│   │   ├── year1.yaml
│   │   ├── year2.yaml
│   │   ├── year3.yaml
│   │   ├── curriculum.yaml
│   │   ├── assignment_bank.yaml
│   │   └── quiz_bank.yaml
│   ├── scenarios/
│   │   └── scenarios.yaml
│   ├── domain/
│   │   ├── tracks.yaml
│   │   ├── scenarios.yaml
│   │   └── assignments.yaml
│   └── ai_pathway/
│       ├── modules.yaml
│       └── project_ladder.yaml
├── docs/
│   ├── IMPLEMENTATION_PLAN.md
│   ├── MASTER_SCOPE.md
│   └── screenshots/
├── scripts/
│   ├── bootstrap.sh
│   ├── bootstrap_kali.sh
│   ├── run_app.sh
│   ├── run_school.sh
│   ├── run_watcher.sh
│   └── scan_imports.sh
├── storage/
│   ├── import_materials/
│   ├── quarantine/
│   └── logs/scans/
├── src/last_dices_terminal_school/
│   ├── main.py
│   ├── setup_seed.py
│   ├── import_cli.py
│   ├── watch_imports.py
│   ├── app/
│   │   ├── school_app.py
│   │   ├── tui.py
│   │   ├── theme.tcss
│   │   ├── screens/
│   │   └── widgets/
│   ├── core/
│   ├── db/
│   ├── services/
│   ├── engines/
│   ├── ai/
│   └── agents/
├── tests/
└── examples/
```

---

## 2) MVP Definition (First Working Kali-Local Version)

A successful MVP is the smallest serious release that behaves like a school operating system:

1. Bootstraps on Kali locally (no Docker required).
2. Launches terminal UI with navigation and core screens.
3. Seeds a 3-year curriculum into SQLite.
4. Supports lessons, tasks, weekly goals, monthly goals.
5. Supports quizzes + scoring + attempt tracking.
6. Supports assignments + submission + feedback capture.
7. Tracks progress events and basic weak-area indicators.
8. Imports local files into an ingestion pipeline.
9. Scans files defensively (ClamAV when available) and quarantines suspicious items.
10. Exposes AI agents with safe fallback behavior when no model provider is configured.

---

## 3) Phase-by-Phase Roadmap

## Phase 1 — Kali Local Core OS

**Outcome:** clone-and-run terminal school system with defensive defaults.

- TUI shell + navigation + essential screens.
- SQLite schema + repository persistence.
- Curriculum loader + today/weekly/monthly resolution.
- Quiz and assignment core flows.
- Import pipeline + scan status + quarantine behavior.
- Agent scaffolding with deterministic fallback providers.
- Seed setup + bootstrap scripts + baseline tests.

## Phase 2 — Applied Learning Intelligence

**Outcome:** richer school mechanics and adaptive guidance.

- Milestone reviews, retry loops, and review prompts.
- Stronger weak-domain detection and remediation pathways.
- Expanded rubric-driven assignment feedback and resubmission loops.
- Improved dashboard analytics and readiness signals.
- Deeper scenario linking across logistics/maritime/supply-chain tracks.
- Expanded AI engineering project ladder and evaluation exercises.

## Phase 3 — Specialization + Company Readiness

**Outcome:** portfolio-quality capability system aligned with Last Dices Pty Ltd goals.

- Domain readiness scoring and specialization progression gates.
- Case-study packaging and evidence-based progress reporting.
- Internal defensive tool-building tracks (authorized environments only).
- Structured outputs for future service offerings in logistics cybersecurity.
- Extension points for optional local web/desktop companion interfaces.

---

## 4) What Must Work Immediately After Cloning

1. `bash scripts/bootstrap.sh` creates venv, installs deps, prepares storage dirs.
2. `python -m last_dices_terminal_school.setup_seed` initializes DB and seed data.
3. `bash scripts/run_school.sh` or `bash scripts/run_app.sh` starts TUI.
4. `bash scripts/run_watcher.sh` monitors import folder.
5. `bash scripts/scan_imports.sh` executes manual import scan/index flow.
6. If ClamAV is missing, scanning fails safely and logs actionable warnings.
7. Unit tests execute with `pytest -q` once dependencies are installed.

---

## 5) Component Allocation by Phase

## Phase 1 Components (must-have)

- App entrypoint + TUI shell
- Sidebar nav + core screens (dashboard/curriculum/lesson/quiz/assignments/resources/import/scanner/agents/settings)
- SQLite schema/repository core tables
- Curriculum engine (3-year hierarchy + progression basics)
- Quiz + assignment base services
- Progress events + reports baseline
- Defensive import + scanning pipeline
- AI service abstraction + six specialized agent scaffolds
- Scripts + seed + tests + operational README

## Phase 2 Components (should-have)

- Richer lesson note workflows and milestone review UX
- Advanced weak-area detection and adaptive planning
- Enhanced scoring dimensions and feedback explainability
- Expanded domain scenario mapping and analysis loops
- Better historical trend and readiness dashboards

## Phase 3 Components (strategic)

- Production-grade specialization readiness model
- Case-study to portfolio publishing workflow (local-first)
- Company-aligned output templates (defensive services)
- Pluggable model backends and advanced evaluation pipeline
- Future desktop/web companion adapters

---

## Safety Boundary (applies to every phase)

This system is for defensive education and authorized ethical learning only.

Out of scope:
- malware creation
- exploit automation
- credential theft
- persistence tooling
- destructive attack implementation
- unauthorized intrusion workflows
