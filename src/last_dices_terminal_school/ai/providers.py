from __future__ import annotations

from last_dices_terminal_school.ai.contracts import ModelProvider, PromptMessage


class NullProvider(ModelProvider):
    """Safe default when no model backend is configured."""

    name = "null-provider"

    def generate(self, messages: list[PromptMessage], temperature: float = 0.2) -> str:
        user_msg = next((m.content for m in reversed(messages) if m.role == "user"), "")
        return (
            "Model unavailable. Returning deterministic coaching output. "
            f"Focus on: {user_msg[:180]}"
        )


class EchoProvider(ModelProvider):
    """Simple local testing provider; replace with local LLM or API adapter later."""

    name = "echo-provider"

    def generate(self, messages: list[PromptMessage], temperature: float = 0.2) -> str:
        merged = " | ".join([f"{m.role}:{m.content[:100]}" for m in messages])
        return f"ECHO::{merged}"
