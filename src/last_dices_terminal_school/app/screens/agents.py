from textual.app import ComposeResult
from textual.widgets import Static

from last_dices_terminal_school.app.screens.base import BaseSchoolScreen
from last_dices_terminal_school.ai.contracts import AgentRequest


class AgentsScreen(BaseSchoolScreen):
    mode_name = "AI AGENTS"

    def body(self) -> ComposeResult:
        lesson_resp = self.app.agent_hub.for_lesson("Linux shell survival", weak_areas="permissions")
        quiz_resp = self.app.agent_hub.for_quiz_review("Network segmentation and defensive monitoring")
        assign_resp = self.app.agent_hub.for_assignment_feedback("I wrote a containment and detection plan for supplier phishing.")
        reflect_resp = self.app.agent_hub.for_scenario_reflection("warehouse ransomware")
        ai_builder_resp = self.app.agent_hub.run(
            AgentRequest(
                agent_name="ai_builder",
                objective="AI pathway coaching",
                context=self.app.ai_pathway_service.ai_builder_context(),
            )
        )

        lines = [
            "AGENT STAFF LAYER",
            "=================",
            "Study Coach       -> lesson planning and daily breakdown",
            "Quiz Master       -> objective practice generation + wrong answer explanations",
            "Assignment Marker -> structured grading + improvement notes",
            "Logistics Mentor  -> logistics/maritime/supply-chain defensive context",
            "AI Builder        -> AI engineering + secure tool-building guidance",
            "Red Blue Reflector-> conceptual attacker-vs-defender reflection (defensive only)",
            "",
            "LOCAL SERVICE READY",
            "-------------------",
            f"Provider: {self.app.ai_service.provider.name} (safe default if no model)",
            "No provider lock-in. Replace provider with local model/API adapter later.",
            "",
            "EXAMPLE CALL OUTPUTS",
            "--------------------",
            f"Study Coach: {lesson_resp.summary}",
            f"Quiz Master: {quiz_resp.summary}",
            f"Assignment Marker: {assign_resp.summary}",
            f"Red Blue Reflector: {reflect_resp.summary}",
            f"AI Builder: {ai_builder_resp.summary}",
            "",
            "PLUG POINTS",
            "-----------",
            "- Lesson screen -> Study Coach",
            "- Quiz screen -> Quiz Master",
            "- Assignments/Submissions -> Assignment Marker",
            "- Scenarios -> Logistics Mentor + Red Blue Reflector",
            "- AI track modules -> AI Builder",
        ]

        yield Static("\n".join(lines), classes="panel")
