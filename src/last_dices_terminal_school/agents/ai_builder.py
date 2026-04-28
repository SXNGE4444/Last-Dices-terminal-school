from last_dices_terminal_school.agents.base import BaseAgent
from last_dices_terminal_school.ai.contracts import AgentRequest


class AIBuilderAgent(BaseAgent):
    name = "ai_builder"

    def build_user_prompt(self, request: AgentRequest) -> str:
        goal = request.context.get("goal", request.objective)
        return f"Given goal '{goal}', propose AI build steps, architecture checks, and safety checkpoints."
