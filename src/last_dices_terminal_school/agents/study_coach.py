from last_dices_terminal_school.agents.base import BaseAgent
from last_dices_terminal_school.ai.contracts import AgentRequest


class StudyCoachAgent(BaseAgent):
    name = "study_coach"

    def build_user_prompt(self, request: AgentRequest) -> str:
        lesson = request.context.get("lesson_title", request.objective)
        minutes = request.context.get("minutes", 60)
        weak = request.context.get("weak_areas", "none")
        return f"Create a daily plan for lesson '{lesson}' with {minutes} minutes and weak areas: {weak}."
