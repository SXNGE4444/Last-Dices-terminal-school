from pathlib import Path

from last_dices_terminal_school.core.school_models import ProgressEventModel
from last_dices_terminal_school.db.repository import SchoolRepository
from last_dices_terminal_school.db.schema import init_db
from last_dices_terminal_school.services.progress_service import ProgressService


def test_progress_events_logged(tmp_path: Path) -> None:
    db = tmp_path / "school.db"
    init_db(db)
    repo = SchoolRepository(db)
    service = ProgressService(repo)

    service.log(
        ProgressEventModel(
            event_type="lesson_started",
            lesson_id="y1-l-001",
            module_id="y1-m1-linux-network",
            details={"source": "test"},
        )
    )
    summary = service.summary()
    assert summary.get("lesson_started", 0) >= 1
