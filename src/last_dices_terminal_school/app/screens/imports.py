from textual.app import ComposeResult
from textual.widgets import Static

from last_dices_terminal_school.app.screens.base import BaseSchoolScreen
from last_dices_terminal_school.app.widgets.design_system import status_marker, terminal_table


class ImportsScreen(BaseSchoolScreen):
    mode_name = "INTAKE QUEUE"

    def body(self) -> ComposeResult:
        rows = []
        if getattr(self.app, "repo", None):
            rows = [[status.upper(), path] for path, status, _ in self.app.repo.latest_scan_logs(limit=8)]

        table = terminal_table(["Status", "Path"], rows or [["NONE", "No scan activity yet"]])

        yield Static(
            "IMPORT CONTROL\n==============\n"
            "Queue folder : ./import_materials\n"
            "Quarantine   : ./quarantine\n"
            "Scan logs    : ./logs/scans/scan.log\n\n"
            + status_marker("ok", "Monitored intake queue active")
            + "\n"
            + status_marker("warn", "Only clean files are indexed")
            + "\n"
            + status_marker("err", "Suspicious files move to quarantine")
            + "\n\nRECENT INTAKE EVENTS\n--------------------\n"
            + table,
            classes="panel",
        )
