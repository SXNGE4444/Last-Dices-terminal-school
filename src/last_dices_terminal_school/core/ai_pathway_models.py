from __future__ import annotations

from typing import Literal

from pydantic import BaseModel


Level = Literal["beginner", "intermediate", "advanced"]


class AIPracticeTask(BaseModel):
    id: str
    title: str
    level: Level
    objective: str
    estimated_minutes: int


class AIAssignment(BaseModel):
    id: str
    module_id: str
    title: str
    prompt: str
    deliverables: list[str]


class AIProjectStep(BaseModel):
    id: str
    stage: int
    title: str
    outcome: str


class AIModule(BaseModel):
    id: str
    level: Level
    title: str
    topics: list[str]
    practice_tasks: list[AIPracticeTask]
    assignments: list[AIAssignment]


class AITrackBundle(BaseModel):
    modules: list[AIModule]
    project_ladder: list[AIProjectStep]
    model_building_pathway: list[str]
    tool_building_pathway: list[str]
    cybersecurity_tool_building_pathway: list[str]
