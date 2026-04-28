from textual.widgets import Static


class SidebarNav(Static):
    def __init__(self) -> None:
        super().__init__(id="sidebar")

    def render(self) -> str:
        return (
            "TERMINAL SCHOOL SHELL\n"
            "=====================\n"
            "[1] Dashboard\n"
            "[2] Curriculum\n"
            "[3] Lesson Briefing\n"
            "[4] Quiz Station\n"
            "[5] Assignment Console\n"
            "[6] Submissions\n"
            "[7] Resource Library\n"
            "[8] Import Queue\n"
            "[9] Scanner Pane\n"
            "[0] Scenario Lab\n"
            "[a] Agent Desk\n"
            "[s] Settings\n"
            "[d] Home\n"
            "[q] Quit\n"
            "\n"
            "QUICK ACTIONS\n"
            "-------------\n"
            "[ START ] [ SUBMIT ] [ REVIEW ]\n"
            "\n"
            "STATUS\n"
            "------\n"
            "[OK] School runtime\n"
            "[OK] Local-first mode\n"
            "[WARN] External model optional\n"
            "[LOCKED] Defensive-only scope"
        )
