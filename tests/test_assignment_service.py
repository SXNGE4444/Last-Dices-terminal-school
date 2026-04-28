from pathlib import Path

from last_dices_terminal_school.core.school_models import AssignmentSubmissionModel
from last_dices_terminal_school.db.repository import SchoolRepository
from last_dices_terminal_school.db.schema import init_db
from last_dices_terminal_school.services.assignment_service import AssignmentService


def test_submit_and_grade_assignment(tmp_path: Path) -> None:
    db = tmp_path / "school.db"
    init_db(db)
    repo = SchoolRepository(db)
    service = AssignmentService(repo, Path("data/curriculum/assignment_bank.yaml"))

    submission = AssignmentSubmissionModel(
        assignment_id="y1-asg-001",
        module_id="y1-m1-linux-network",
        content="This response explains control evidence and detect/contain plans for logistics operations.",
    )
    result = service.submit_and_grade(submission)
    assert result.total_score > 0
    assert repo.assignment_history("y1-asg-001")
