from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static

from last_dices_terminal_school.app.screens.base import BaseSchoolScreen
from last_dices_terminal_school.app.widgets.design_system import progress_bar, status_marker, terminal_table


class DashboardScreen(BaseSchoolScreen):
    mode_name = "MISSION CONTROL"

    def body(self) -> ComposeResult:
        seed = self.app.seed_data
        lesson = seed.lessons()[0] if seed.lessons() else {"title": "No lesson loaded", "track": "N/A"}
        weekly = seed.goals("weekly")[:3]
        monthly = seed.goals("monthly")[:3]
        tasks = seed.tasks()[:4]

        progress = min(100, int((len(tasks) / 10) * 100))
        event_summary = self.app.progress_service.summary() if getattr(self.app, "progress_service", None) else {}

        goals_table = terminal_table(
            ["Scope", "Goal", "Target"],
            [["WEEK", g["title"], str(g["target_value"])] for g in weekly]
            + [["MONTH", g["title"], str(g["target_value"])] for g in monthly],
        )

        with Horizontal(classes="row"):
            yield Static(
                "BRIEFING PANE\n=============\n"
                f"Lesson : {lesson.get('title')}\n"
                f"Track  : {lesson.get('track')}\n"
                f"Goal   : {lesson.get('objective')}\n"
                + status_marker("ready", "Session open"),
                classes="panel",
            )
            yield Static(
                "TASK QUEUE\n=========\n"
                + "\n".join([f"- {t['title']} [TODO]" for t in tasks])
                + "\n\n"
                + status_marker("ok", "Operator workload balanced"),
                classes="panel",
            )

        with Horizontal(classes="row"):
            yield Static("GOAL BOARD\n==========\n" + goals_table, classes="panel")
            yield Static(
                "SYSTEM PROGRESS\n===============\n"
                f"{progress_bar(progress)}\n"
                f"Quiz attempts      : {event_summary.get('quiz_attempted', 0)}\n"
                f"Assignments        : {event_summary.get('assignment_submitted', 0)}\n"
                f"Lesson completed   : {event_summary.get('lesson_completed', 0)}\n\n"
                + status_marker("ok", "Mission control stable"),
                classes="panel",
            )
