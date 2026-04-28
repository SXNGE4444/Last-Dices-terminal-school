from textual.app import ComposeResult
from textual.widgets import Static

from last_dices_terminal_school.app.screens.base import BaseSchoolScreen
from last_dices_terminal_school.app.widgets.design_system import bracket_button, status_marker, terminal_table


class QuizScreen(BaseSchoolScreen):
    mode_name = "TERMINAL EXAM STATION"

    def body(self) -> ComposeResult:
        quiz_id = "y1-qz-001"
        questions = self.app.quiz_service.questions_for_quiz(quiz_id)
        lines = [f"Quiz ID: {quiz_id}", status_marker("ready", "Objective exam mode"), ""]
        for i, q in enumerate(questions, start=1):
            lines.append(f"Q{i}. {q.question}")
            for c_idx, choice in enumerate(q.choices):
                lines.append(f"   {c_idx}) {choice}")
            lines.append(f"   [REVIEW] Explanation: {q.explanation}")

        history = self.app.quiz_service.score_history(quiz_id)
        weak = self.app.quiz_service.weak_domain_tracking()

        hist_table = terminal_table(
            ["Score", "Timestamp"],
            [[f"{score}%", ts] for score, ts in history[:5]] or [["-", "No attempts"]],
        )
        weak_table = terminal_table(
            ["Domain", "Average", "Risk"],
            [[x["domain"], x["average"], x["risk"].upper()] for x in weak] or [["-", "-", "-"]],
        )

        lines.append("\nSCORE HISTORY\n-------------\n" + hist_table)
        lines.append("\nWEAK DOMAIN MAP\n---------------\n" + weak_table)
        lines.append(
            "\n"
            + bracket_button("start")
            + " "
            + bracket_button("submit")
            + " "
            + bracket_button("review")
            + "\n"
            + status_marker("warn", "Retry recommended if score < 80")
        )

        yield Static("\n".join(lines), classes="panel")
