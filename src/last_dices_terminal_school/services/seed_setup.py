from __future__ import annotations

from pathlib import Path

from last_dices_terminal_school.core.settings import settings
from last_dices_terminal_school.db.repository import SchoolRepository
from last_dices_terminal_school.db.schema import init_db
from last_dices_terminal_school.services.curriculum_loader import CurriculumLoader, ScenarioLoader


class SeedSetupService:
    def __init__(self, db_path: Path | None = None):
        self.db_path = db_path or settings.db_path

    def run(self) -> dict[str, int]:
        init_db(self.db_path)
        repo = SchoolRepository(self.db_path)

        lessons = tasks = goals = assignments = quizzes = scenarios = 0
        if settings.curriculum_file.exists():
            loader = CurriculumLoader(settings.curriculum_file)
            lsn, tsk, gol, asg, qz = loader.load()
            repo.save_lessons([x.model_dump() for x in lsn])
            repo.save_tasks(tsk)
            repo.save_goals(gol)
            repo.save_assignments(asg)
            repo.save_quizzes(qz)
            lessons, tasks, goals, assignments, quizzes = (
                len(lsn),
                len(tsk),
                len(gol),
                len(asg),
                len(qz),
            )

        if settings.scenario_file.exists():
            scn = ScenarioLoader(settings.scenario_file).load()
            repo.save_scenarios(scn)
            scenarios = len(scn)

        return {
            "lessons": lessons,
            "tasks": tasks,
            "goals": goals,
            "assignments": assignments,
            "quizzes": quizzes,
            "scenarios": scenarios,
        }
