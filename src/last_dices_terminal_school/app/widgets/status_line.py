from textual.widgets import Static


class StatusLine(Static):
    def __init__(self, mode: str):
        super().__init__(id="status-line")
        self.mode = mode

    def on_mount(self) -> None:
        self.update(self._render())

    def set_mode(self, mode: str) -> None:
        self.mode = mode
        self.update(self._render())

    def _render(self) -> str:
        return (
            f"MODE:{self.mode}  [OK] LOCAL  [OK] DB  [WARN] OPTIONAL MODEL  "
            "[READY] TRAINING SESSION  [ START ] [ SUBMIT ] [ REVIEW ]"
        )
