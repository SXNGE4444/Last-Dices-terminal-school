from __future__ import annotations

from last_dices_terminal_school.core.models import Report
from last_dices_terminal_school.db.repository import SchoolRepository


class ProgressReportService:
    def __init__(self, repo: SchoolRepository):
        self.repo = repo

    def build_weekly_report(self) -> Report:
        snap = self.repo.dashboard_snapshot()
        summary = (
            f"Progress {int(snap['overall_progress'])}% | "
            f"Tasks {snap['task_done']}/{snap['task_total']} | "
            f"Track {snap['specialization_track']}"
        )
        return Report(
            title="Weekly Defensive Study Report",
            summary=summary,
            strengths=["Consistent terminal practice", "Defensive scenario awareness"],
            next_actions=[
                "Complete one logistics scenario write-up",
                "Submit one assignment with response metrics",
                "Revise networking quiz topics",
            ],
        )

    def save_weekly_report(self) -> Report:
        report = self.build_weekly_report()
        body = (
            f"SUMMARY\n{report.summary}\n\n"
            f"STRENGTHS\n- " + "\n- ".join(report.strengths) + "\n\n"
            f"NEXT ACTIONS\n- " + "\n- ".join(report.next_actions)
        )
        self.repo.save_report(report.title, body)
        return report
