from __future__ import annotations

from abc import ABC, abstractmethod

from last_dices_terminal_school.ai.contracts import AgentRequest, AgentResponse, PromptMessage
from last_dices_terminal_school.ai.service import AIService
from last_dices_terminal_school.agents.prompts.templates import PROMPT_TEMPLATES


class BaseAgent(ABC):
    name = "base"

    def __init__(self, ai_service: AIService):
        self.ai_service = ai_service

    @abstractmethod
    def build_user_prompt(self, request: AgentRequest) -> str:
        raise NotImplementedError

    def run(self, request: AgentRequest) -> AgentResponse:
        tpl = PROMPT_TEMPLATES[self.name]
        messages = [
            PromptMessage(role="system", content=tpl["system"]),
            PromptMessage(role="user", content=self.build_user_prompt(request)),
        ]
        return self.ai_service.run(
            agent_name=self.name,
            messages=messages,
            safety_notes=[
                "Defensive educational use only.",
                "No malware, credential theft, persistence, or exploit execution guidance.",
            ],
        )
