from last_dices_terminal_school.agents.base import BaseAgent
from last_dices_terminal_school.ai.contracts import AgentRequest


class RedBlueReflectorAgent(BaseAgent):
    name = "red_blue_reflector"

    def build_user_prompt(self, request: AgentRequest) -> str:
        scenario = request.context.get("scenario", request.objective)
        return (
            f"Reflect scenario '{scenario}' with conceptual attacker paths and defensive controls. "
            "No exploitation instructions."
        )
