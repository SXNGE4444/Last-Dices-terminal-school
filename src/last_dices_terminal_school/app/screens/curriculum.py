from textual.app import ComposeResult
from textual.widgets import Static

from last_dices_terminal_school.app.screens.base import BaseSchoolScreen


class CurriculumScreen(BaseSchoolScreen):
    mode_name = "CURRICULUM MAP"

    def body(self) -> ComposeResult:
        rows = []
        for lesson in self.app.seed_data.lessons():
            rows.append(f"Y{lesson['year']} | {lesson['track']:<28} | {lesson['id']} | {lesson['title']}")

        ai_bundle = self.app.ai_pathway_service.bundle()
        ai_rows = [f"- [{m.level}] {m.title}" for m in ai_bundle.modules]
        ladder_rows = [f"  {p.stage}. {p.title}" for p in ai_bundle.project_ladder[:4]]

        yield Static(
            "3-YEAR PATHWAY\n==============\n"
            "YEAR 1: Foundations -> Linux / Networking / Cyber basics\n"
            "YEAR 2: Applied -> AI Engineering / AI Systems / Python tools\n"
            "YEAR 3: Specialization -> Logistics / Maritime / Supply Chain defense\n"
            "\nLESSON TABLE\n------------\n"
            + "\n".join(rows)
            + "\n\nAI ENGINEERING TRACK\n-------------------\n"
            + "\n".join(ai_rows)
            + "\n\nAI PROJECT LADDER (top)\n-----------------------\n"
            + "\n".join(ladder_rows),
            classes="panel",
        )
