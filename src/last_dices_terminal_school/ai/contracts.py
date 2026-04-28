from __future__ import annotations

from datetime import datetime
from typing import Any, Protocol

from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    agent_name: str
    objective: str
    context: dict[str, Any] = Field(default_factory=dict)


class AgentResponse(BaseModel):
    agent_name: str
    summary: str
    bullets: list[str] = Field(default_factory=list)
    follow_up_actions: list[str] = Field(default_factory=list)
    safety_notes: list[str] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=datetime.utcnow)


class PromptMessage(BaseModel):
    role: str
    content: str


class ModelProvider(Protocol):
    name: str

    def generate(self, messages: list[PromptMessage], temperature: float = 0.2) -> str:
        ...
