from last_dices_terminal_school.agents.base import BaseAgent
from last_dices_terminal_school.ai.contracts import AgentRequest


class QuizMasterAgent(BaseAgent):
    name = "quiz_master"

    def build_user_prompt(self, request: AgentRequest) -> str:
        summary = request.context.get("lesson_summary", request.objective)
        count = request.context.get("count", 5)
        return f"From lesson summary: {summary}, generate {count} objective questions with answers and explanation notes."
