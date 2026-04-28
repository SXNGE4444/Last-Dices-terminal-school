from textual.app import ComposeResult
from textual.widgets import Static

from last_dices_terminal_school.app.screens.base import BaseSchoolScreen
from last_dices_terminal_school.app.widgets.design_system import bracket_button, status_marker


class LessonScreen(BaseSchoolScreen):
    mode_name = "LESSON BRIEFING PANE"

    def body(self) -> ComposeResult:
        lesson = self.app.seed_data.lessons()[0]
        yield Static(
            "LESSON BRIEF\n============\n"
            f"ID       : {lesson['id']}\n"
            f"Title    : {lesson['title']}\n"
            f"Track    : {lesson['track']}\n"
            f"Duration : {lesson['estimated_minutes']} min\n"
            f"Objective: {lesson['objective']}\n"
            "\nOPERATOR CHECKLIST\n------------------\n"
            "- Review prerequisite notes\n"
            "- Execute authorized defensive lab steps\n"
            "- Capture evidence and reflections\n"
            "- Map lesson output to scenario use\n\n"
            f"{bracket_button('start')} {bracket_button('review')}\n"
            + status_marker("ok", "Briefing ready for execution"),
            classes="panel",
        )
