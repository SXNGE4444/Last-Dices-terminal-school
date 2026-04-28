from pathlib import Path

from last_dices_terminal_school.services.curriculum_loader import CurriculumLoader


def test_curriculum_loader_parses_tasks_and_goals() -> None:
    loader = CurriculumLoader(Path("data/curriculum/curriculum.yaml"))
    lessons, tasks, goals, assignments, quizzes = loader.load()

    assert lessons
    assert tasks
    assert goals
    assert assignments
    assert quizzes
