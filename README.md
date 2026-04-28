# LAST DICES // TERMINAL SCHOOL OS

> A local-first, defensive-by-design learning operating system for building elite cybersecurity and AI engineering capability on Kali Linux.

---

## What this project is

**LAST DICES // TERMINAL SCHOOL OS** is a terminal-native school platform that combines:

- structured multi-year curriculum delivery,
- practical assignment and quiz workflows,
- local data persistence,
- defensive material ingestion with malware scanning,
- and an AI-agent support layer for guided learning.

It is not a "tutorial repo." It is the foundation of a long-term operating system for disciplined capability building and company formation.

## Why this exists

Most learning stacks are fragmented: docs in one place, notes elsewhere, no consistent progression model, and no operational discipline around safety.

This project exists to solve that by providing a **single local system** where a learner can:

1. execute a defined mission over years (not weeks),
2. track progress in defensible, auditable ways,
3. learn cybersecurity and AI engineering together,
4. operate with security-first defaults from day one.

## Who this is for

This system is designed for:

- serious self-directed builders,
- early-stage technical founders,
- defensive cybersecurity practitioners,
- AI engineers building secure tooling,
- and apprentices training for real operations in logistics/supply-chain environments.

If you want quick hacks or offensive payload workflows, this project is not for you.

---

## 3-Year mission

The mission is to produce an operator who can:

- design and run a defensive cybersecurity program,
- build internal security tooling with AI assistance,
- and transition those capabilities into a company-grade service organization.

### Year 1 — Foundation and discipline

- Linux operations, Python, networking, security fundamentals
- repeatable study cadence, assignment completion, and quiz performance
- defensive scanning and local-first workflow habits

### Year 2 — Systems and specialization

- scenario-driven training for logistics/supply-chain/maritime-adjacent defense
- deeper architecture and incident response reasoning
- AI-assisted workflows for productivity, analysis, and reporting

### Year 3 — Production and company readiness

- building deployable internal tools
- measurable domain readiness
- operational transition toward commercial capability under Last Dices Pty Ltd

---

## Strategic goals

### Logistics cybersecurity specialization goal

Build a practitioner profile capable of defending:

- warehouse and freight workflows,
- supplier and partner interfaces,
- shipment/manifest data chains,
- maritime-adjacent operational systems,
- and associated cloud/API surfaces.

The curriculum and domain scenarios are designed to move from conceptual understanding to operational decision quality.

### AI engineering goal

Build a practitioner who can:

- design secure AI-assisted workflows,
- build practical agent/tool systems,
- evaluate model behavior and outputs,
- and integrate AI into defensive operations without compromising safety controls.

### Last Dices Pty Ltd vision

LAST DICES // TERMINAL SCHOOL OS is the capability engine behind a larger company vision:

> **Last Dices Pty Ltd** becomes a high-trust, defense-focused logistics cybersecurity and AI engineering organization, built from first-principles training, local operational rigor, and long-horizon execution.

---

## Major features

- **Terminal-native school UI** with multi-screen workflow (dashboard, curriculum, assignments, quizzes, imports, scans, agents).
- **Local SQLite school system** for lessons, tasks, goals, assignments, quizzes, submissions, reports, and import scan records.
- **Curriculum + scenario loaders** from YAML sources to keep content explicit and versioned.
- **Assignment and quiz engines** with structured service layers.
- **AI agent layer** with safe default providers (`NullProvider`, `EchoProvider`) and extension points for local/API model backends.
- **Material ingestion pipeline** with status tracking (`pending`, `scanning`, `clean`, `quarantined`, `failed`).
- **Defensive malware scanning integration** through ClamAV (`clamscan`) with quarantine handling.
- **Seed/setup utilities** for local bootstrap and repeatable data initialization.

---

## Local-first Kali usage

This project is intentionally optimized for **local Kali Linux usage**:

- run directly from terminal,
- keep primary state in local SQLite,
- use local folders for imports, quarantine, and logs,
- avoid cloud dependency for core operation,
- prioritize deterministic behavior over remote complexity.

### Defensive file scanning model

All ingested learning materials should be treated as untrusted by default.

- Files enter `import_materials/`
- Scanner evaluates file safety (via `clamscan` when available)
- Clean files are indexed
- Suspicious or failed scans are quarantined
- Logs are written under `logs/scans/`

This is defensive hygiene, not malware analysis tooling.

---

## School system structure

At a high level, the system has five layers:

1. **Content layer** — YAML curriculum, scenario, domain, and pathway data.
2. **Domain model layer** — Pydantic models for curriculum, imports, school entities, and AI pathway.
3. **Service/engine layer** — curriculum, assignments, quizzes, imports, reporting, progress, domain readiness.
4. **Persistence layer** — SQLite schema + repository APIs.
5. **Interface layer** — terminal app screens/widgets and command entrypoints.

---

## Screenshots

> Replace placeholders with actual captures as the UI stabilizes.

### Dashboard
![Dashboard Placeholder](docs/screenshots/dashboard-placeholder.png)

### Curriculum / Lesson View
![Curriculum Placeholder](docs/screenshots/curriculum-placeholder.png)

### Assignment / Quiz Flow
![Assessment Placeholder](docs/screenshots/assessment-placeholder.png)

### Import + Scan Operations
![Scan Placeholder](docs/screenshots/scan-placeholder.png)

### Agent Desk
![Agents Placeholder](docs/screenshots/agents-placeholder.png)

---

## Install instructions

### Prerequisites

- Python **3.11+**
- Kali Linux (recommended target environment)
- `git`
- Optional but recommended: `clamav` (`clamscan`)

### 1) Clone

```bash
git clone <your-repo-url>
cd Last-Dices-terminal-school
```

### 2) Configure environment (optional)

```bash
cp .env.example .env
```

Edit `.env` if you want custom storage paths. By default, all runtime state lives under `./storage`.

### 3) Bootstrap

Recommended:

```bash
bash scripts/bootstrap.sh
```

Or install as an editable package:

```bash
python -m pip install -e .[dev]
```

Kali helper script (if you prefer distro-specific setup):

```bash
bash scripts/bootstrap_kali.sh
```

### 4) Activate environment (if needed)

```bash
source .venv/bin/activate
```

---

## Run instructions

### Run the school app

```bash
bash scripts/run_school.sh
```

or

```bash
bash scripts/run_app.sh
```

or direct module run:

```bash
python -m last_dices_terminal_school.main
```

### Run import watcher

```bash
bash scripts/run_watcher.sh
```

### Manual import scan helper

```bash
bash scripts/scan_imports.sh
```

### Seed setup manually

```bash
python -m last_dices_terminal_school.setup_seed
```

### Run tests

```bash
pytest -q
```

### Optional Make targets

```bash
make run
make watch
make seed
make test
```

---

## Repository structure

```text
.
├── data/                              # Curriculum, pathway, scenarios, domain assets
├── storage/                           # Local runtime state (db, imports, quarantine, logs)
├── scripts/                           # Bootstrap + runtime helpers
├── src/last_dices_terminal_school/
│   ├── agents/                        # Learning/support agent personas + hub
│   ├── ai/                            # AI contracts, providers, service abstraction
│   ├── app/                           # Terminal UI app, screens, widgets, theme
│   ├── core/                          # Pydantic models + settings
│   ├── db/                            # SQLite schema + repository
│   ├── engines/                       # Core assignment/quiz evaluation engines
│   ├── services/                      # Curriculum, domain, imports, reporting, progress
│   ├── import_cli.py                  # Import CLI entrypoint
│   ├── setup_seed.py                  # Seed setup entrypoint
│   ├── watch_imports.py               # Import watcher entrypoint
│   └── main.py                        # Main app entrypoint
├── tests/                             # Unit tests by subsystem
├── requirements.txt
├── pyproject.toml
├── Makefile
├── pytest.ini
└── README.md
```

---

## Roadmap

### Current phase

- Stable local-first skeleton
- curriculum + service pipelines in place
- test-backed core modules

### Near-term priorities

- richer TUI workflows and user state transitions
- stronger reporting/analytics outputs
- deeper curriculum progression logic and gating
- improved local model integration path
- screenshot and demo artifacts for each major screen

### Mid-term priorities

- stronger assignment rubric intelligence
- readiness scorecards by specialization track
- operational playbook integration for domain scenarios
- internal API hardening and plugin extension model

---

## Safety scope (strict)

This repository is for **defensive cybersecurity education and authorized training only**.

Out of scope:

- exploit automation,
- malware development,
- credential theft,
- unauthorized access workflows,
- destructive payload guidance,
- persistence/stealth tradecraft for misuse.

If a capability increases misuse risk, it should be excluded or redesigned defensively.

---

## Future phases

### Phase 1 — Local operator OS

Solidify the terminal school experience as a reliable, daily-use training system.

### Phase 2 — Team training system

Support multi-operator workflows, shared scenario packs, and review pipelines while keeping defensive controls first.

### Phase 3 — Company capability stack

Transform learning outputs into real service capability:

- logistics cybersecurity programs,
- AI-enabled defensive operations tooling,
- measurable security outcomes for client environments.

### Phase 4 — Last Dices institutional platform

Evolve from a training OS into an institutional-grade operating platform for Last Dices Pty Ltd’s long-horizon mission.

---

## Project direction statement

LAST DICES // TERMINAL SCHOOL OS is being built as a serious long-term system.

The objective is not a demo. The objective is operational readiness, technical depth, and disciplined execution that compounds into a real company.
