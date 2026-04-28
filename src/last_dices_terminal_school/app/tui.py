from __future__ import annotations

from pathlib import Path

from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Footer, Header, Static

from last_dices_terminal_school.core.settings import settings
from last_dices_terminal_school.db.repository import SchoolRepository
from last_dices_terminal_school.db.schema import init_db
from last_dices_terminal_school.services.curriculum_loader import CurriculumLoader, ScenarioLoader
from last_dices_terminal_school.services.reporting import ProgressReportService


class LastDicesSchoolApp(App):
    TITLE = "LAST DICES // TERMINAL SCHOOL OS"
    SUB_TITLE = "Local-First Defensive Cyber + AI School"

    CSS = """
    Screen {
        background: #050705;
        color: #33ff66;
    }
    Header, Footer {
        background: #071007;
        color: #33ff66;
    }
    #root {
        padding: 1;
    }
    .panel {
        border: solid #2faa4b;
        padding: 1;
        height: 1fr;
    }
    """

    BINDINGS = [
        ("r", "generate_report", "Generate report"),
        ("q", "quit", "Quit"),
    ]

    def __init__(self) -> None:
        super().__init__()
        init_db(settings.db_path)
        self.repo = SchoolRepository(settings.db_path)
        self.report_service = ProgressReportService(self.repo)
        self._load_seed_data()

    def _load_seed_data(self) -> None:
        if Path(settings.curriculum_file).exists():
            loader = CurriculumLoader(settings.curriculum_file)
            lessons, tasks, goals, assignments, quizzes = loader.load()
            self.repo.save_lessons([l.model_dump() for l in lessons])
            self.repo.save_tasks(tasks)
            self.repo.save_goals(goals)
            self.repo.save_assignments(assignments)
            self.repo.save_quizzes(quizzes)

        if Path(settings.scenario_file).exists():
            scenarios = ScenarioLoader(settings.scenario_file).load()
            self.repo.save_scenarios(scenarios)

    def compose(self) -> ComposeResult:
        snap = self.repo.dashboard_snapshot()
        progress = int(snap["overall_progress"])

        lessons = self.repo.list_lessons()
        assignments = self.repo.list_assignments()
        quizzes = self.repo.list_quizzes()
        resources = self.repo.list_resources()
        reports = self.repo.latest_reports()

        yield Header(show_clock=True)
        with Container(id="root"):
            with Horizontal():
                yield Static(
                    self._block(
                        "DASHBOARD // TODAY",
                        [
                            f"Learner : {snap['learner_name']}",
                            f"Lesson  : {snap['today_lesson']}",
                            f"Track   : {snap['today_track']}",
                            f"Spec    : {snap['specialization_track']}",
                        ],
                    ),
                    classes="panel",
                )
                yield Static(
                    self._block("GOALS // WEEK", [f"- {x}" for x in snap["weekly_goals"]]),
                    classes="panel",
                )
                yield Static(
                    self._block("GOALS // MONTH", [f"- {x}" for x in snap["monthly_goals"]]),
                    classes="panel",
                )

            with Horizontal():
                yield Static(
                    self._block(
                        "PROGRESS",
                        [
                            self._bar(progress),
                            f"Completion : {progress}%",
                            f"Tasks      : {snap['task_done']}/{snap['task_total']}",
                            f"Lessons    : {snap['lesson_count']}",
                        ],
                    ),
                    classes="panel",
                )
                yield Static(self._block("LESSON RAIL", [f"{i} | Y{y} | {t}" for i, t, y in lessons]), classes="panel")

            with Horizontal():
                yield Static(
                    self._block("ASSIGNMENTS", [f"{i} :: {t}" for i, t in assignments]),
                    classes="panel",
                )
                yield Static(
                    self._block("QUIZZES", [f"{i} :: {t}" for i, t in quizzes]),
                    classes="panel",
                )

            with Horizontal():
                yield Static(
                    self._block(
                        "RESOURCE LIBRARY",
                        [f"{status:<12} {path}" for path, status in resources]
                        or ["No imported materials yet."],
                    ),
                    classes="panel",
                )
                yield Static(
                    self._block(
                        "REPORTS",
                        [f"{created} | {title}" for title, created in reports]
                        or ["Press [r] to generate weekly report."],
                    ),
                    classes="panel",
                )

            with Vertical():
                yield Static(
                    Text.from_markup(
                        "[bold]SCENARIO DEFENSE RAIL[/bold]\n"
                        "- warehouse ransomware\n"
                        "- supplier phishing\n"
                        "- shipping manifest tampering\n"
                        "- customs workflow disruption\n"
                        "- maritime navigation integrity issue\n"
                        "- contractor laptop compromise"
                    ),
                    classes="panel",
                )
        yield Footer()

    def action_generate_report(self) -> None:
        report = self.report_service.save_weekly_report()
        self.notify(f"Saved report: {report.title}")

    @staticmethod
    def _bar(percent: int, width: int = 40) -> str:
        done = int((percent / 100) * width)
        return "[" + ("#" * done) + ("-" * (width - done)) + "]"

    @staticmethod
    def _block(title: str, rows: list[str]) -> str:
        return "\n".join([title, "=" * len(title), *rows])
