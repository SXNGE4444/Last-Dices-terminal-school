# LAST DICES // TERMINAL SCHOOL OS — Implementation Plan

## 1) Full Repository Structure

```text
.
├── README.md
├── requirements.txt
├── pyproject.toml
├── Makefile
├── .env.example
├── data/
├── docs/
│   ├── IMPLEMENTATION_PLAN.md
│   └── screenshots/
├── storage/
│   ├── import_materials/
│   ├── quarantine/
│   └── logs/scans/
├── scripts/
├── src/last_dices_terminal_school/
└── tests/
```

## 2) MVP Scope (Serious Starter)

- Terminal-first learning workflow with dashboard, curriculum, assignments, quizzes, imports, scans, and agent workspace.
- SQLite-backed persistence for lessons, goals, tasks, submissions, attempts, resource indexing, and reports.
- 3-year curriculum and domain scenarios preloaded from YAML.
- Defensive ingestion with ClamAV integration and quarantine-first behavior.
- Specialized agent scaffolding for study, quizzes, assignment feedback, domain mentoring, and AI-builder guidance.

## 3) Phase Plan

### Phase 1: Foundation OS
- Bootstrapping, local storage layout, seed loading, and TUI navigation.

### Phase 2: Training Depth
- Better lesson progression, rubric-driven grading, weak-domain loops, and improved reporting.

### Phase 3: Domain Specialization
- Logistics/maritime/supply-chain specialization tracks with scenario drills and readiness metrics.

### Phase 4: Company Readiness
- Portfolio-grade case studies, operational playbooks, and tool-building tracks aligned with Last Dices Pty Ltd.

## 4) Code Skeleton Priorities

- Keep services modular and test-driven.
- Preserve safe defaults for all AI and scanning integrations.
- Add extension points for local model adapters and future desktop/web clients.
