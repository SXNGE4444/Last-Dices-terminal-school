from __future__ import annotations

from pathlib import Path

import yaml

from last_dices_terminal_school.core.curriculum_models import (
    CourseModel,
    CurriculumModel,
    ModuleModel,
    ProgressState,
)


class CurriculumEngine:
    def __init__(self, curriculum: CurriculumModel):
        self.curriculum = curriculum
        self.modules = {
            module.id: module
            for course in curriculum.courses
            for module in course.modules
        }

    @classmethod
    def load_from_directory(cls, directory: Path) -> "CurriculumEngine":
        manifest_path = directory / "manifest.yaml"
        manifest = yaml.safe_load(manifest_path.read_text())

        courses: list[CourseModel] = []
        for year_file in manifest["years"]:
            payload = yaml.safe_load((directory / year_file).read_text())
            courses.append(CourseModel(**payload["course"]))

        curriculum = CurriculumModel(
            school_name=str(manifest.get("school_name", "LAST DICES // TERMINAL SCHOOL OS")),
            version=str(manifest.get("version", "1.0")),
            school_name=manifest.get("school_name", "LAST DICES // TERMINAL SCHOOL OS"),
            version=manifest.get("version", "1.0"),
            courses=courses,
        )
        return cls(curriculum)

    def unlocked_modules(self, progress: ProgressState) -> list[ModuleModel]:
        unlocked = []
        for module in self.modules.values():
            if all(pr in progress.completed_modules for pr in module.prerequisites):
                unlocked.append(module)
        return sorted(unlocked, key=lambda m: (m.year, m.id))

    def locked_modules(self, progress: ProgressState) -> list[ModuleModel]:
        unlocked_ids = {m.id for m in self.unlocked_modules(progress)}
        return [m for m in self.modules.values() if m.id not in unlocked_ids]

    def todays_lesson(self, progress: ProgressState):
        unlocked = self.unlocked_modules(progress)
        for module in unlocked:
            for lesson in module.lessons:
                if lesson.id not in progress.completed_lessons:
                    return lesson
        return None

    def next_task(self, progress: ProgressState):
        unlocked = self.unlocked_modules(progress)
        for module in unlocked:
            for plan in module.weekly_plans:
                if plan.week_number < progress.current_week:
                    continue
                tasks = plan.daily_tasks.get(progress.current_day, [])
                for task in tasks:
                    if task.lesson_id is None or task.lesson_id not in progress.completed_lessons:
                        return task
        return None

    def next_assignment(self, progress: ProgressState):
        unlocked = self.unlocked_modules(progress)
        assignments = [
            assignment
            for module in unlocked
            for assignment in module.assignments
            if assignment.id not in progress.completed_assignments
        ]
        if not assignments:
            return None
        return sorted(assignments, key=lambda a: a.due_week)[0]

    def weak_area_detection(self, progress: ProgressState) -> list[dict[str, str]]:
        areas: dict[str, list[float]] = {}

        quiz_index = {
            q.id: q.track
            for module in self.modules.values()
            for q in module.quizzes
        }

        for quiz_id, score in progress.quiz_scores.items():
            track = quiz_index.get(quiz_id, "general")
            areas.setdefault(track, []).append(score)

        findings = []
        for track, scores in areas.items():
            avg = sum(scores) / len(scores)
            if avg < 70:
                findings.append(
                    {
                        "track": track,
                        "severity": "high",
                        "reason": f"average quiz score {avg:.1f}% is below 70%",
                        "recommendation": "schedule review block + scenario drill",
                    }
                )
            elif avg < 80:
                findings.append(
                    {
                        "track": track,
                        "severity": "medium",
                        "reason": f"average quiz score {avg:.1f}% needs improvement",
                        "recommendation": "add one extra practice quiz this week",
                    }
                )

        if not findings:
            findings.append(
                {
                    "track": "overall",
                    "severity": "ok",
                    "reason": "no weak areas detected from available scores",
                    "recommendation": "continue progression and monthly review",
                }
            )
        return findings
