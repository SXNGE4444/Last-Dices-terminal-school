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
