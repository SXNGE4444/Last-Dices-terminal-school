from __future__ import annotations

from last_dices_terminal_school.agents.ai_builder import AIBuilderAgent
from last_dices_terminal_school.agents.assignment_marker import AssignmentMarkerAgent
from last_dices_terminal_school.agents.logistics_mentor import LogisticsMentorAgent
from last_dices_terminal_school.agents.quiz_master import QuizMasterAgent
from last_dices_terminal_school.agents.red_blue_reflector import RedBlueReflectorAgent
from last_dices_terminal_school.agents.study_coach import StudyCoachAgent
from last_dices_terminal_school.ai.contracts import AgentRequest, AgentResponse
from last_dices_terminal_school.ai.service import AIService


class AgentHub:
    def __init__(self, ai_service: AIService):
        self.agents = {
            "study_coach": StudyCoachAgent(ai_service),
            "quiz_master": QuizMasterAgent(ai_service),
            "assignment_marker": AssignmentMarkerAgent(ai_service),
            "logistics_mentor": LogisticsMentorAgent(ai_service),
            "ai_builder": AIBuilderAgent(ai_service),
            "red_blue_reflector": RedBlueReflectorAgent(ai_service),
        }

    def run(self, request: AgentRequest) -> AgentResponse:
        if request.agent_name not in self.agents:
            raise ValueError(f"Unknown agent {request.agent_name}")
        return self.agents[request.agent_name].run(request)

    def for_lesson(self, lesson_title: str, weak_areas: str = "") -> AgentResponse:
        return self.run(
            AgentRequest(
                agent_name="study_coach",
                objective="daily lesson plan",
                context={"lesson_title": lesson_title, "minutes": 60, "weak_areas": weak_areas},
            )
        )

    def for_quiz_review(self, lesson_summary: str) -> AgentResponse:
        return self.run(
            AgentRequest(
                agent_name="quiz_master",
                objective="practice quiz",
                context={"lesson_summary": lesson_summary, "count": 5},
            )
        )

    def for_assignment_feedback(self, submission_text: str) -> AgentResponse:
        return self.run(
            AgentRequest(
                agent_name="assignment_marker",
                objective="grade submission",
                context={"submission_text": submission_text},
            )
        )

    def for_scenario_reflection(self, scenario: str) -> AgentResponse:
        return self.run(
            AgentRequest(
                agent_name="red_blue_reflector",
                objective="defensive reflection",
                context={"scenario": scenario},
            )
        )
