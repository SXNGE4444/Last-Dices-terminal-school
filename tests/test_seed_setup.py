from pathlib import Path

from last_dices_terminal_school.core.settings import settings
from last_dices_terminal_school.services.seed_setup import SeedSetupService


def test_seed_setup_service_loads_curriculum_and_scenarios(tmp_path, monkeypatch):
    curriculum_path = tmp_path / "curriculum.yaml"
    scenario_path = tmp_path / "scenarios.yaml"
    db_path = tmp_path / "school.db"

    curriculum_path.write_text(
        """
lessons:
  - id: L1
    year: 1
    track: core
    title: Linux Foundations
    objective: Build command-line confidence

tasks:
  - id: T1
    lesson_id: L1
    title: Practice shell navigation

goals:
  - id: G1
    scope: weekly
    title: Complete lesson 1

assignments:
  - id: A1
    lesson_id: L1
    title: Hardening checklist
    prompt: Write a baseline host hardening plan
    rubric: [clarity, completeness]

quizzes:
  - id: Q1
    lesson_id: L1
    title: Linux basics quiz
    questions:
      - question: Which command prints current directory?
        choices: [ls, pwd, cd]
        answer_index: 1
""".strip()
    )

    scenario_path.write_text(
        """
scenarios:
  - id: S1
    title: Warehouse phishing incident
    severity: medium
""".strip()
    )

    monkeypatch.setattr(settings, "curriculum_file", curriculum_path)
    monkeypatch.setattr(settings, "scenario_file", scenario_path)

    counts = SeedSetupService(db_path=db_path).run()

    assert counts == {
        "lessons": 1,
        "tasks": 1,
        "goals": 1,
        "assignments": 1,
        "quizzes": 1,
        "scenarios": 1,
    }
    assert Path(db_path).exists()
