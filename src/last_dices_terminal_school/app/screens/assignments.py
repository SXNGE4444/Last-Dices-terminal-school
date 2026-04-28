from textual.app import ComposeResult
from textual.widgets import Static

from last_dices_terminal_school.app.screens.base import BaseSchoolScreen
from last_dices_terminal_school.app.widgets.design_system import bracket_button, status_marker


class AssignmentsScreen(BaseSchoolScreen):
    mode_name = "TRAINING CONSOLE"

    def body(self) -> ComposeResult:
        prompts = self.app.assignment_service.list_prompts()
        lines = [
            "ASSIGNMENT OPERATION FLOW",
            "-------------------------",
            "1) Select assignment",
            "2) Draft response in terminal notes",
            "3) Submit locally for marker feedback",
            "4) Review dimension scores",
            "5) Improve and resubmit",
            "",
            "PROMPTS",
            "-------",
        ]
        for p in prompts:
            lines.append(f"- {p['id']} [{p['module_id']}] :: {p['title']}")
            lines.append(f"  prompt: {p['prompt']}")
            lines.append(f"  dimensions: {', '.join(p['dimensions'])}")

        domain_assignments = self.app.domain_service.assignments_by_track("logistics")
        lines.append("\nDOMAIN ASSIGNMENTS (logistics)")
        lines.append("-----------------------------")
        for da in domain_assignments[:3]:
            lines.append(f"- {da.id} :: {da.title}")
            lines.append(f"  scenario: {da.scenario_id}")
            lines.append("  deliverables: " + ", ".join(da.defensive_deliverables[:2]))

        history = self.app.assignment_service.score_history("y1-asg-001")
        lines.append("\nSUBMISSION HISTORY (y1-asg-001)")
        lines.append("------------------------------")
        lines.extend([f"- {score}% at {ts}" for score, ts in history[:5]] or ["No submissions yet."])
        lines.append(
            "\nFeedback format: summary + strengths + improvement_suggestions + dimension scores"
        )
        lines.append(
            "\n"
            + bracket_button("submit")
            + " "
            + bracket_button("review")
            + "\n"
            + status_marker("ok", "Training console ready")
        )

        yield Static("\n".join(lines), classes="panel")
