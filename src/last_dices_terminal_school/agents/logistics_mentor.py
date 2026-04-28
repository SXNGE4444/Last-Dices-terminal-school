from last_dices_terminal_school.agents.base import BaseAgent
from last_dices_terminal_school.ai.contracts import AgentRequest


class LogisticsMentorAgent(BaseAgent):
    name = "logistics_mentor"

    def build_user_prompt(self, request: AgentRequest) -> str:
        concept = request.context.get("concept", request.objective)
        return f"Explain how concept '{concept}' impacts logistics reality and defensive controls."
