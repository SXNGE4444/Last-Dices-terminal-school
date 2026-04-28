from __future__ import annotations

from pathlib import Path

import yaml

from last_dices_terminal_school.core.ai_pathway_models import (
    AIAssignment,
    AIModule,
    AIPracticeTask,
    AIProjectStep,
    AITrackBundle,
)


class AIPathwayService:
    def __init__(self, modules_path: Path, ladder_path: Path):
        modules_payload = yaml.safe_load(modules_path.read_text())
        ladder_payload = yaml.safe_load(ladder_path.read_text())

        modules: list[AIModule] = []
        for m in modules_payload.get("modules", []):
            m["practice_tasks"] = [AIPracticeTask(**t) for t in m.get("practice_tasks", [])]
            m["assignments"] = [AIAssignment(**a) for a in m.get("assignments", [])]
            modules.append(AIModule(**m))

        ladder = [AIProjectStep(**s) for s in ladder_payload.get("project_ladder", [])]
        self.bundle_data = AITrackBundle(
            modules=modules,
            project_ladder=ladder,
            model_building_pathway=ladder_payload.get("model_building_pathway", []),
            tool_building_pathway=ladder_payload.get("tool_building_pathway", []),
            cybersecurity_tool_building_pathway=ladder_payload.get("cybersecurity_tool_building_pathway", []),
        )

    def bundle(self) -> AITrackBundle:
        return self.bundle_data

    def modules_by_level(self, level: str) -> list[AIModule]:
        return [m for m in self.bundle_data.modules if m.level == level]

    def project_ladder(self) -> list[AIProjectStep]:
        return sorted(self.bundle_data.project_ladder, key=lambda p: p.stage)

    def ai_builder_context(self) -> dict:
        top_module = self.bundle_data.modules[0].title if self.bundle_data.modules else "AI pathway"
        next_project = self.project_ladder()[0].title if self.project_ladder() else "No project"
        return {
            "goal": f"Advance through {top_module} and deliver project: {next_project}",
            "pathway": " -> ".join([p.title for p in self.project_ladder()[:4]]),
        }
