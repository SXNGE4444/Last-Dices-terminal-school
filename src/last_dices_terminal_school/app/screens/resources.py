from textual.app import ComposeResult
from textual.widgets import Static

from last_dices_terminal_school.app.screens.base import BaseSchoolScreen


class ResourcesScreen(BaseSchoolScreen):
    mode_name = "RESOURCE LIBRARY"

    def body(self) -> ComposeResult:
        rows = []
        if getattr(self.app, "repo", None):
            rows = [f"{status:<12} {path}" for path, status in self.app.repo.list_resources(limit=10)]

        yield Static(
            "RESOURCE LIBRARY (SAFE INDEX)\n=============================\n"
            "Only clean files are indexed with metadata + topic tags.\n"
            "Topics: linux, networking, security, logistics, maritime, supply-chain, AI, Python\n\n"
            "INDEXED MATERIALS\n-----------------\n"
            + ("\n".join(rows) if rows else "No clean materials indexed yet."),
            classes="panel",
        )
