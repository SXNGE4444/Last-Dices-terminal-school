from __future__ import annotations

from pathlib import Path

import yaml

from last_dices_terminal_school.core.domain_models import (
    CaseStudy,
    DefensiveAnalysisQuestion,
    DomainAssignmentPrompt,
    DomainBundle,
    DomainLessonModule,
    DomainReadinessReport,
    ScenarioCard,
)
from last_dices_terminal_school.db.repository import SchoolRepository


class DomainService:
    def __init__(
        self,
        repo: SchoolRepository,
        scenarios_path: Path,
        tracks_path: Path,
        assignments_path: Path,
    ):
        self.repo = repo
        scn_payload = yaml.safe_load(scenarios_path.read_text())
        trk_payload = yaml.safe_load(tracks_path.read_text())
        asg_payload = yaml.safe_load(assignments_path.read_text())

        self.scenarios = [
            ScenarioCard(
                **{
                    **s,
                    "analysis_questions": [DefensiveAnalysisQuestion(**q) for q in s.get("analysis_questions", [])],
                }
            )
            for s in scn_payload.get("scenarios", [])
        ]
        self.modules = [DomainLessonModule(**m) for m in trk_payload.get("modules", [])]
        self.case_studies = [CaseStudy(**c) for c in trk_payload.get("case_studies", [])]
        self.assignments = [DomainAssignmentPrompt(**a) for a in asg_payload.get("assignments", [])]

    def bundle(self) -> DomainBundle:
        return DomainBundle(
            modules=self.modules,
            scenarios=self.scenarios,
            case_studies=self.case_studies,
            assignments=self.assignments,
        )

    def scenarios_by_track(self, track: str) -> list[ScenarioCard]:
        return [s for s in self.scenarios if s.track == track]

    def assignments_by_track(self, track: str) -> list[DomainAssignmentPrompt]:
        return [a for a in self.assignments if a.track == track]

    def readiness_reports(self) -> list[DomainReadinessReport]:
        weak_domains = self.repo.weak_domains()
        track_map = {
            "linux-network": "logistics",
            "applied-cyber-ai": "supply_chain",
            "logistics-maritime-supply": "maritime",
            "logistics-cyber": "logistics",
            "maritime-awareness": "maritime",
            "supply-chain-defense": "supply_chain",
        }

        grouped: dict[str, list[float]] = {"logistics": [], "maritime": [], "supply_chain": []}
        for domain, avg, _attempts in weak_domains:
            grouped[track_map.get(domain, "supply_chain")].append(avg)

        reports: list[DomainReadinessReport] = []
        for track, scores in grouped.items():
            avg = sum(scores) / len(scores) if scores else 0.0
            weak_topics = []
            if avg < 70:
                weak_topics = ["incident triage", "integrity validation", "vendor-risk controls"]
            elif avg < 80:
                weak_topics = ["evidence depth", "scenario reasoning"]
            else:
                weak_topics = ["none-critical"]

            recommendations = [
                "Run one scenario drill this week",
                "Submit one assignment revision with stronger control mapping",
                "Document measurable detection metrics",
            ]
            reports.append(
                DomainReadinessReport(
                    track=track,  # type: ignore[arg-type]
                    average_score=round(avg, 2),
                    weak_topics=weak_topics,
                    recommendations=recommendations,
                )
            )

        return reports
