from __future__ import annotations

from last_dices_terminal_school.ai.contracts import AgentResponse, ModelProvider, PromptMessage
from last_dices_terminal_school.ai.providers import NullProvider


class AIService:
    def __init__(self, provider: ModelProvider | None = None):
        self.provider = provider or NullProvider()

    def run(self, agent_name: str, messages: list[PromptMessage], safety_notes: list[str] | None = None) -> AgentResponse:
        text = self.provider.generate(messages)
        bullets = [line.strip("- ") for line in text.split(".") if line.strip()][:4]
        return AgentResponse(
            agent_name=agent_name,
            summary=text,
            bullets=bullets,
            follow_up_actions=["Record output in notes", "Apply to current module task"],
            safety_notes=safety_notes or ["Defensive and authorized learning contexts only."],
        )
