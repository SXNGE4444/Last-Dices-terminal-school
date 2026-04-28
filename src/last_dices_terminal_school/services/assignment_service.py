from __future__ import annotations

from pathlib import Path

import yaml

from last_dices_terminal_school.core.school_models import (
    AssignmentResultModel,
    AssignmentSubmissionModel,
    FeedbackModel,
    GradingDimensions,
)
from last_dices_terminal_school.db.repository import SchoolRepository


class AssignmentService:
    def __init__(self, repo: SchoolRepository, prompt_bank_path: Path):
        self.repo = repo
        payload = yaml.safe_load(prompt_bank_path.read_text())
        self.prompts = payload.get("assignments", [])

    def list_prompts(self) -> list[dict]:
        return self.prompts

    def submit_and_grade(self, submission: AssignmentSubmissionModel) -> AssignmentResultModel:
        dims = self._score_dimensions(submission.content)
        total = round(
            (
                dims.clarity
                + dims.completeness
                + dims.technical_accuracy
                + dims.reasoning
                + dims.defensive_quality
                + dims.logistics_domain_relevance
            )
            / 6,
            2,
        )

        feedback = FeedbackModel(
            summary=f"Submission scored {total}/100. Focus next on reasoning depth and domain specificity.",
            strengths=[
                "Defensive framing present",
                "Structured response format",
            ],
            improvement_suggestions=[
                "Add clearer evidence for technical claims",
                "Tie controls to logistics operations impact",
                "Include measurable verification steps",
            ],
        )

        result = AssignmentResultModel(
            submission=submission,
            dimensions=dims,
            total_score=total,
            feedback=feedback,
        )

        self.repo.save_assignment_submission(
            assignment_id=submission.assignment_id,
            module_id=submission.module_id,
            scenario_id=submission.scenario_id,
            content=submission.content,
            notes_path=submission.notes_path,
            feedback_json=result.feedback.model_dump_json(),
            dimensions_json=result.dimensions.model_dump_json(),
            total_score=result.total_score,
            improved_from_submission_id=submission.improved_from_submission_id,
        )
        return result

    def score_history(self, assignment_id: str) -> list[tuple[float, str]]:
        return self.repo.assignment_history(assignment_id)

    def _score_dimensions(self, content: str) -> GradingDimensions:
        words = len(content.split())
        def contains(term: str) -> int:
            return 1 if term in content.lower() else 0
        clarity = min(100.0, 45 + words * 0.2)
        completeness = min(100.0, 40 + words * 0.25)
        technical_accuracy = 55 + 10 * contains("control") + 10 * contains("evidence")
        reasoning = 50 + 10 * contains("because") + 10 * contains("therefore")
        defensive_quality = 50 + 15 * contains("detect") + 15 * contains("contain")
        logistics_domain_relevance = 45 + 10 * contains("logistics") + 10 * contains("supply") + 10 * contains("maritime")

        return GradingDimensions(
            clarity=round(min(100.0, clarity), 2),
            completeness=round(min(100.0, completeness), 2),
            technical_accuracy=round(min(100.0, technical_accuracy), 2),
            reasoning=round(min(100.0, reasoning), 2),
            defensive_quality=round(min(100.0, defensive_quality), 2),
            logistics_domain_relevance=round(min(100.0, logistics_domain_relevance), 2),
        )
