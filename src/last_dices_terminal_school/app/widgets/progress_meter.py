from textual.widgets import Static

from last_dices_terminal_school.app.widgets.design_system import progress_bar


class ProgressMeter(Static):
    def __init__(self, percent: int, label: str = "Progress", **kwargs):
        super().__init__(**kwargs)
        self.percent = percent
        self.label = label

    def render(self) -> str:
        return f"{self.label}: {progress_bar(self.percent)}"
