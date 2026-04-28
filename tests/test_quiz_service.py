from pathlib import Path

from last_dices_terminal_school.db.repository import SchoolRepository
from last_dices_terminal_school.db.schema import init_db
from last_dices_terminal_school.services.quiz_service import QuizService


def test_quiz_attempt_and_history(tmp_path: Path) -> None:
    db = tmp_path / "school.db"
    init_db(db)
    repo = SchoolRepository(db)
    service = QuizService(repo, Path("data/curriculum/quiz_bank.yaml"))

    attempt = service.attempt_quiz("y1-qz-001", [1, 1])
    assert attempt.score >= 0
    assert service.score_history("y1-qz-001")
