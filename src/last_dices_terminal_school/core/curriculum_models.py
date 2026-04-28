from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class LessonModel(BaseModel):
    id: str
    module_id: str
    title: str
    objective: str
    estimated_minutes: int = Field(default=60, ge=15)
    quiz_id: str | None = None


class DailyTaskModel(BaseModel):
    id: str
    title: str
    lesson_id: str | None = None
    kind: Literal["study", "practice", "review", "lab", "reflection"] = "study"
    estimated_minutes: int = Field(default=30, ge=10)


class WeeklyPlanModel(BaseModel):
    id: str
    week_number: int
    module_id: str
    focus: str
    daily_tasks: dict[str, list[DailyTaskModel]]
    weekly_review: str


class AssignmentModel(BaseModel):
    id: str
    module_id: str
    title: str
    prompt: str
    due_week: int
    rubric: list[str]


class QuizModel(BaseModel):
    id: str
    module_id: str
    title: str
    track: str
    pass_score: float = 70.0


class ScenarioModel(BaseModel):
    id: str
    module_id: str
    title: str
    track: str
    domain: Literal["logistics", "maritime", "supply_chain", "general"]
    summary: str


class ModuleModel(BaseModel):
    id: str
    year: int
    course_id: str
    title: str
    track: str
    prerequisites: list[str] = Field(default_factory=list)
    monthly_review: str
    lessons: list[LessonModel]
    assignments: list[AssignmentModel]
    quizzes: list[QuizModel]
    scenarios: list[ScenarioModel]
    weekly_plans: list[WeeklyPlanModel]


class CourseModel(BaseModel):
    id: str
    year: int
    title: str
    description: str
    modules: list[ModuleModel]


class CurriculumModel(BaseModel):
    school_name: str
    version: str
    courses: list[CourseModel]


class ProgressState(BaseModel):
    completed_lessons: list[str] = Field(default_factory=list)
    completed_modules: list[str] = Field(default_factory=list)
    completed_assignments: list[str] = Field(default_factory=list)
    quiz_scores: dict[str, float] = Field(default_factory=dict)
    assignment_scores: dict[str, float] = Field(default_factory=dict)
    current_week: int = 1
    current_day: Literal["mon", "tue", "wed", "thu", "fri", "sat", "sun"] = "mon"
