from pathlib import Path

from last_dices_terminal_school.core.curriculum_models import ProgressState
from last_dices_terminal_school.services.curriculum_engine import CurriculumEngine


def test_progression_and_queries() -> None:
    engine = CurriculumEngine.load_from_directory(Path("data/curriculum"))
    progress = ProgressState(current_week=1, current_day="mon")

    unlocked = engine.unlocked_modules(progress)
    assert unlocked
    assert unlocked[0].id == "y1-m1-linux-network"
    assert engine.todays_lesson(progress) is not None
    assert engine.next_task(progress) is not None
    assert engine.next_assignment(progress) is not None


def test_weak_area_detection() -> None:
    engine = CurriculumEngine.load_from_directory(Path("data/curriculum"))
    progress = ProgressState(quiz_scores={"y1-qz-001": 62.0, "y2-qz-001": 69.0})

    findings = engine.weak_area_detection(progress)
    assert findings
    assert findings[0]["severity"] in {"high", "medium", "ok"}
