from pathlib import Path

from last_dices_terminal_school.db.repository import SchoolRepository
from last_dices_terminal_school.db.schema import init_db
from last_dices_terminal_school.services.domain_service import DomainService


def test_domain_bundle_and_tracks(tmp_path: Path) -> None:
    db = tmp_path / "school.db"
    init_db(db)
    repo = SchoolRepository(db)
    service = DomainService(
        repo,
        Path("data/domain/scenarios.yaml"),
        Path("data/domain/tracks.yaml"),
        Path("data/domain/assignments.yaml"),
    )

    bundle = service.bundle()
    assert bundle.scenarios
    assert service.scenarios_by_track("logistics")
    assert service.assignments_by_track("supply_chain")
