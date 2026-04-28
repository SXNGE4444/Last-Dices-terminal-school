from pathlib import Path
from textual.app import App

from last_dices_terminal_school.app.screens.agents import AgentsScreen
from last_dices_terminal_school.app.screens.assignments import AssignmentsScreen
from last_dices_terminal_school.app.screens.curriculum import CurriculumScreen
from last_dices_terminal_school.app.screens.dashboard import DashboardScreen
from last_dices_terminal_school.app.screens.imports import ImportsScreen
from last_dices_terminal_school.app.screens.lesson import LessonScreen
from last_dices_terminal_school.app.screens.malware_scan import MalwareScanScreen
from last_dices_terminal_school.app.screens.quiz import QuizScreen
from last_dices_terminal_school.app.screens.resources import ResourcesScreen
from last_dices_terminal_school.app.screens.scenarios import ScenariosScreen
from last_dices_terminal_school.app.screens.settings import SettingsScreen
from last_dices_terminal_school.app.screens.submissions import SubmissionsScreen
from last_dices_terminal_school.core.settings import settings
from last_dices_terminal_school.db.repository import SchoolRepository
from last_dices_terminal_school.db.schema import init_db
from last_dices_terminal_school.services.clamav_scanner import ClamAVScanner
from last_dices_terminal_school.services.material_import_service import MaterialImportService
from last_dices_terminal_school.services.quiz_service import QuizService
from last_dices_terminal_school.services.assignment_service import AssignmentService
from last_dices_terminal_school.services.progress_service import ProgressService
from last_dices_terminal_school.services.ui_seed import UISeedData
from last_dices_terminal_school.services.domain_service import DomainService
from last_dices_terminal_school.services.ai_pathway_service import AIPathwayService
from last_dices_terminal_school.ai.service import AIService
from last_dices_terminal_school.agents.hub import AgentHub


class LastDicesSchoolApp(App):
    TITLE = "LAST DICES // TERMINAL SCHOOL OS"
    SUB_TITLE = "Terminal-first defensive cyber & AI school"
    CSS_PATH = "theme.tcss"

    BINDINGS = [
        ("1", "go('dashboard')", "Dashboard"),
        ("2", "go('curriculum')", "Curriculum"),
        ("3", "go('lesson')", "Lesson"),
        ("4", "go('quiz')", "Quiz"),
        ("5", "go('assignments')", "Assignments"),
        ("6", "go('submissions')", "Submissions"),
        ("7", "go('resources')", "Resources"),
        ("8", "go('imports')", "Imports"),
        ("9", "go('malware')", "Malware Scan"),
        ("0", "go('scenarios')", "Scenarios"),
        ("a", "go('agents')", "Agents"),
        ("s", "go('settings')", "Settings"),
        ("d", "go('dashboard')", "Dashboard"),
        ("q", "quit", "Quit"),
    ]

    SCREENS = {
        "dashboard": DashboardScreen,
        "curriculum": CurriculumScreen,
        "lesson": LessonScreen,
        "quiz": QuizScreen,
        "assignments": AssignmentsScreen,
        "submissions": SubmissionsScreen,
        "resources": ResourcesScreen,
        "imports": ImportsScreen,
        "malware": MalwareScanScreen,
        "scenarios": ScenariosScreen,
        "agents": AgentsScreen,
        "settings": SettingsScreen,
    }

    def on_mount(self) -> None:
        init_db(settings.db_path)
        self.repo = SchoolRepository(settings.db_path)
        self.scanner = ClamAVScanner(settings.quarantine_dir, settings.scans_dir)
        self.importer = MaterialImportService(self.repo, self.scanner)
        self.seed_data = UISeedData(settings.curriculum_file, settings.scenario_file)
        self.quiz_service = QuizService(self.repo, Path("data/curriculum/quiz_bank.yaml"))
        self.assignment_service = AssignmentService(self.repo, Path("data/curriculum/assignment_bank.yaml"))
        self.progress_service = ProgressService(self.repo)
        self.domain_service = DomainService(
            self.repo,
            Path("data/domain/scenarios.yaml"),
            Path("data/domain/tracks.yaml"),
            Path("data/domain/assignments.yaml"),
        )
        self.ai_pathway_service = AIPathwayService(
            Path("data/ai_pathway/modules.yaml"),
            Path("data/ai_pathway/project_ladder.yaml"),
        )
        self.ai_service = AIService()
        self.agent_hub = AgentHub(self.ai_service)
        self.push_screen("dashboard")

    def action_go(self, target: str) -> None:
        if target in self.SCREENS:
            self.switch_screen(target)
