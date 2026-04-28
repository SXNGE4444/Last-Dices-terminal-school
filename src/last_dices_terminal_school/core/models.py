from __future__ import annotations

from datetime import date
from typing import Literal

from pydantic import BaseModel, Field


class Lesson(BaseModel):
    id: str
    year: int
    track: str
    title: str
    objective: str
    estimated_minutes: int = Field(default=60, ge=10)


class Task(BaseModel):
    id: str
    lesson_id: str
    title: str
    status: Literal["todo", "in_progress", "done"] = "todo"


class Goal(BaseModel):
    id: str
    scope: Literal["weekly", "monthly"]
    title: str
    target_value: int = 1


class Assignment(BaseModel):
    id: str
    lesson_id: str
    title: str
    prompt: str
    rubric: list[str] = Field(default_factory=list)


class QuizQuestion(BaseModel):
    question: str
    choices: list[str]
    answer_index: int


class Quiz(BaseModel):
    id: str
    lesson_id: str
    title: str
    questions: list[QuizQuestion]


class Submission(BaseModel):
    assignment_id: str
    content: str
    submitted_on: date


class Feedback(BaseModel):
    score: float = Field(ge=0, le=100)
    strengths: list[str]
    improvements: list[str]
    marker_agent: Literal["assignment_marker", "quiz_master", "study_coach"]


class Report(BaseModel):
    title: str
    summary: str
    strengths: list[str]
    next_actions: list[str]
