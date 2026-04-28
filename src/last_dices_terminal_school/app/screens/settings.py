from textual.app import ComposeResult
from textual.widgets import Static

from last_dices_terminal_school.app.screens.base import BaseSchoolScreen


class SettingsScreen(BaseSchoolScreen):
    mode_name = "SETTINGS"

    def body(self) -> ComposeResult:
        yield Static(
            "SYSTEM SETTINGS\n===============\n"
            "Theme            : green-on-near-black\n"
            "Database         : ~/.last_dices_terminal_school/school.db\n"
            "Import folder    : ./import_materials\n"
            "Quarantine folder: ./quarantine\n"
            "Safety mode      : [LOCKED] defensive-only\n"
            "API mode         : local optional\n\n"
            "Keyboard help: 1..0/a/s navigation, d dashboard, q quit",
            classes="panel",
        )
