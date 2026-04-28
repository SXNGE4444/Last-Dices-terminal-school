from textual.app import ComposeResult
from textual.widgets import Static

from last_dices_terminal_school.app.screens.base import BaseSchoolScreen


class ScenariosScreen(BaseSchoolScreen):
    mode_name = "DOMAIN SCENARIO LAB"

    def body(self) -> ComposeResult:
        bundle = self.app.domain_service.bundle()
        lines = [
            "TRACKS: logistics | maritime | supply_chain",
            "All cards are defensive, analytical, and authorized-context educational scenarios.",
            "",
        ]

        for card in bundle.scenarios[:6]:
            lines.append(f"[{card.track}] {card.title}")
            lines.append(f"env: {card.environment}")
            lines.append(f"summary: {card.summary}")
            lines.append("defensive controls: " + ", ".join(card.defensive_controls[:3]))
            lines.append("analysis questions:")
            for q in card.analysis_questions[:2]:
                lines.append(f" - {q.question} ({q.focus})")
            lines.append("")

        reports = self.app.domain_service.readiness_reports()
        lines.append("DOMAIN READINESS MAP")
        lines.append("--------------------")
        for report in reports:
            lines.append(
                f"- {report.track}: avg {report.average_score} | weak areas: {', '.join(report.weak_topics)}"
            )

        yield Static("\n".join(lines), classes="panel")
