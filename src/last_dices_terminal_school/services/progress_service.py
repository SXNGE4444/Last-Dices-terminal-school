from __future__ import annotations

import json

from last_dices_terminal_school.core.school_models import ProgressEventModel
from last_dices_terminal_school.db.repository import SchoolRepository


class ProgressService:
    def __init__(self, repo: SchoolRepository):
        self.repo = repo

    def log(self, event: ProgressEventModel) -> None:
        self.repo.add_progress_event(
            event_type=event.event_type,
            lesson_id=event.lesson_id,
            module_id=event.module_id,
            details_json=json.dumps(event.details),
        )

    def summary(self) -> dict[str, int]:
        return self.repo.progress_summary()
