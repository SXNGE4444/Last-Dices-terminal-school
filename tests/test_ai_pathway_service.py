from pathlib import Path

from last_dices_terminal_school.services.ai_pathway_service import AIPathwayService


def test_ai_pathway_bundle() -> None:
    service = AIPathwayService(
        Path("data/ai_pathway/modules.yaml"),
        Path("data/ai_pathway/project_ladder.yaml"),
    )
    bundle = service.bundle()
    assert bundle.modules
    assert bundle.project_ladder
    assert service.modules_by_level("beginner")
