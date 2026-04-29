from __future__ import annotations

from pathlib import Path

import yaml

from last_dices_terminal_school.core.models import Assignment, Goal, Lesson, Quiz, QuizQuestion, Task
from last_dices_terminal_school.services.curriculum_engine import CurriculumEngine


class CurriculumLoader:
    def __init__(self, curriculum_path: Path):
        self.curriculum_path = curriculum_path

    def load(self) -> tuple[list[Lesson], list[Task], list[Goal], list[Assignment], list[Quiz]]:
        data = yaml.safe_load(self.curriculum_path.read_text())
        lessons = [Lesson(**item) for item in data.get("lessons", [])]
        tasks = [Task(**item) for item in data.get("tasks", [])]
        goals = [Goal(**item) for item in data.get("goals", [])]
        assignments = [Assignment(**item) for item in data.get("assignments", [])]

        quizzes: list[Quiz] = []
        for q in data.get("quizzes", []):
            q["questions"] = [QuizQuestion(**qq) for qq in q["questions"]]
            quizzes.append(Quiz(**q))

        return lessons, tasks, goals, assignments, quizzes


class ScenarioLoader:
    def __init__(self, scenario_path: Path):
        self.scenario_path = scenario_path

    def load(self) -> list[dict[str, str]]:
        data = yaml.safe_load(self.scenario_path.read_text())
        return data.get("scenarios", [])


def load_curriculum_engine(curriculum_dir: Path) -> CurriculumEngine:
    return CurriculumEngine.load_from_directory(curriculum_dir)
