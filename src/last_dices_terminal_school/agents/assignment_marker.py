from last_dices_terminal_school.agents.base import BaseAgent
from last_dices_terminal_school.ai.contracts import AgentRequest


class AssignmentMarkerAgent(BaseAgent):
    name = "assignment_marker"

    def build_user_prompt(self, request: AgentRequest) -> str:
        text = request.context.get("submission_text", request.objective)
        return f"Review submission text and provide structured feedback. Submission: {text}"
