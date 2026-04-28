from pathlib import Path

from last_dices_terminal_school.db.repository import SchoolRepository
from last_dices_terminal_school.db.schema import init_db
from last_dices_terminal_school.services.reporting import ProgressReportService


def test_report_creation(tmp_path: Path) -> None:
    db_path = tmp_path / "school.db"
    init_db(db_path)
    repo = SchoolRepository(db_path)

    service = ProgressReportService(repo)
    report = service.save_weekly_report()

    assert "Weekly" in report.title
    assert repo.latest_reports(limit=1)
