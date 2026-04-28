from __future__ import annotations

from pathlib import Path

import yaml


class UISeedData:
    def __init__(self, curriculum_path: Path, scenario_path: Path):
        self.curriculum_path = curriculum_path
        self.scenario_path = scenario_path
        self.curriculum = self._load_yaml(curriculum_path)
        self.scenarios = self._load_yaml(scenario_path)

    @staticmethod
    def _load_yaml(path: Path) -> dict:
        if not path.exists():
            return {}
        return yaml.safe_load(path.read_text()) or {}

    def lessons(self) -> list[dict]:
        return self.curriculum.get("lessons", [])

    def tasks(self) -> list[dict]:
        return self.curriculum.get("tasks", [])

    def goals(self, scope: str) -> list[dict]:
        return [x for x in self.curriculum.get("goals", []) if x.get("scope") == scope]

    def assignments(self) -> list[dict]:
        return self.curriculum.get("assignments", [])

    def quizzes(self) -> list[dict]:
        return self.curriculum.get("quizzes", [])

    def scenario_rows(self) -> list[dict]:
        return self.scenarios.get("scenarios", [])
