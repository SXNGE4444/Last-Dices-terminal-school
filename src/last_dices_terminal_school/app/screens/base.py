from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Footer, Header, Static

from last_dices_terminal_school.app.widgets.sidebar import SidebarNav
from last_dices_terminal_school.app.widgets.status_line import StatusLine


class BaseSchoolScreen(Screen):
    mode_name = "UNKNOWN"

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal(id="shell"):
            yield SidebarNav()
            with Vertical(id="workspace"):
                yield Static(f"{self.mode_name}\n{'=' * len(self.mode_name)}", id="screen-title")
                yield StatusLine(self.mode_name)
                yield from self.body()
        yield Footer()

    def body(self) -> ComposeResult:
        yield Static("No content")
