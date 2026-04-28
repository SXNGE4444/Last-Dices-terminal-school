from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class ObjectiveQuestion(BaseModel):
    id: str
    quiz_id: str
    module_id: str
    lesson_id: str
    domain: str
    question: str
    choices: list[str]
    answer_index: int
    explanation: str


class QuizAttemptModel(BaseModel):
    quiz_id: str
    lesson_id: str
    module_id: str
    domain: str
    answers: list[int]
    score: float
    passed: bool
    explanations: list[str]
    attempted_at: datetime = Field(default_factory=datetime.utcnow)


class GradingDimensions(BaseModel):
    clarity: float
    completeness: float
    technical_accuracy: float
    reasoning: float
    defensive_quality: float
    logistics_domain_relevance: float


class FeedbackModel(BaseModel):
    summary: str
    strengths: list[str]
    improvement_suggestions: list[str]


class AssignmentSubmissionModel(BaseModel):
    assignment_id: str
    module_id: str
    scenario_id: str | None = None
    content: str
    notes_path: str | None = None
    improved_from_submission_id: int | None = None


class AssignmentResultModel(BaseModel):
    submission: AssignmentSubmissionModel
    dimensions: GradingDimensions
    total_score: float
    feedback: FeedbackModel


class ProgressEventModel(BaseModel):
    event_type: Literal[
        "lesson_started",
        "lesson_completed",
        "notes_written",
        "quiz_attempted",
        "quiz_passed",
        "assignment_submitted",
        "assignment_improved",
    ]
    lesson_id: str | None = None
    module_id: str | None = None
    details: dict = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)
