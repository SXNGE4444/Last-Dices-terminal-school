# Current Status

All known duplicate-patch regressions are resolved in source files:

- `services/curriculum_engine.py` has a single `CurriculumModel(...)` block with string-cast `school_name` and `version`.
- `db/repository.py` has a single clean `save_scenarios(...)` block with `focus` normalization.
- `services/assignment_service.py` keeps only `def contains(...)` in `_score_dimensions` and no unused `json` import.
- `services/reporting.py` keeps one `NEXT ACTIONS` section in report body assembly.
- `app/tui.py` keeps one `save_lessons([lesson.model_dump() for lesson in lessons])` line.
- `app/theme.tcss` has no unsupported `@media` block.

Current blockers are environment/runtime setup only:

- `.venv` activation path may be missing in this execution environment.
- Python dependencies (`pydantic`, `textual`, pytest extras) may not be installed in the active interpreter.
All previously reported duplicate-patch regressions have been resolved in-source:

- curriculum manifest fields are string-cast before model validation
- scenario persistence normalizes missing `focus`
- assignment scoring helper keeps only typed `contains()`
- reporting keeps a single `NEXT ACTIONS` section
- TUI seed path keeps a single `save_lessons` line
- settings include `storage_root`
- Textual theme has no unsupported `@media` block

Remaining runtime blockers in this execution environment are dependency/setup related:

- virtualenv not present at `.venv/`
- `pydantic` and `textual` not installed in the active interpreter
