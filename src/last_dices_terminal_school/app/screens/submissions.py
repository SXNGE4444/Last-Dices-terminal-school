from textual.app import ComposeResult
from textual.widgets import Static

from last_dices_terminal_school.app.screens.base import BaseSchoolScreen


class SubmissionsScreen(BaseSchoolScreen):
    mode_name = "SUBMISSIONS"

    def body(self) -> ComposeResult:
        yield Static(
            "SUBMISSION LOG\n==============\n"
            "Latest items:\n"
            "- a-y1-linux-001 :: score 72 [WARN] expand control depth\n"
            "- a-y3-logi-201 :: score 88 [OK] strong containment section\n"
            "- a-y3-supply-203 :: [READY] draft pending\n\n"
            "AI MARKING\n----------\n"
            "Assignment Marker agent checks:\n"
            "1) Defensive quality\n2) Clarity\n3) Logistics relevance\n4) Incident response maturity",
            classes="panel",
        )
