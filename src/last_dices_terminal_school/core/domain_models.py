from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


DomainTrack = Literal["logistics", "maritime", "supply_chain"]


class DefensiveAnalysisQuestion(BaseModel):
    id: str
    question: str
    focus: str


class ScenarioCard(BaseModel):
    id: str
    title: str
    track: DomainTrack
    environment: str
    summary: str
    key_assets: list[str]
    likely_risks: list[str]
    defensive_controls: list[str]
    analysis_questions: list[DefensiveAnalysisQuestion]


class CaseStudy(BaseModel):
    id: str
    title: str
    track: DomainTrack
    context: str
    learning_objectives: list[str]
    lessons_learned: list[str]


class DomainLessonModule(BaseModel):
    id: str
    track: DomainTrack
    title: str
    objectives: list[str]
    linked_scenarios: list[str]
    assignments: list[str]


class DomainAssignmentPrompt(BaseModel):
    id: str
    track: DomainTrack
    scenario_id: str
    title: str
    prompt: str
    defensive_deliverables: list[str]


class DomainBundle(BaseModel):
    modules: list[DomainLessonModule]
    scenarios: list[ScenarioCard]
    case_studies: list[CaseStudy]
    assignments: list[DomainAssignmentPrompt]


class DomainReadinessReport(BaseModel):
    track: DomainTrack
    average_score: float
    weak_topics: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
