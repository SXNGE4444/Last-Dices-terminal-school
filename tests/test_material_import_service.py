from pathlib import Path

from last_dices_terminal_school.core.import_models import ScanResultModel, ScanStatus
from last_dices_terminal_school.db.repository import SchoolRepository
from last_dices_terminal_school.db.schema import init_db
from last_dices_terminal_school.services.material_import_service import MaterialImportService


class FakeScanner:
    def scan_file(self, file_path: Path) -> ScanResultModel:
        return ScanResultModel(file_path=file_path, status=ScanStatus.clean, details="OK")


def test_import_service_indexes_clean_file(tmp_path: Path) -> None:
    db = tmp_path / "school.db"
    init_db(db)
    repo = SchoolRepository(db)
    importer = MaterialImportService(repo=repo, scanner=FakeScanner())

    sample = tmp_path / "linux_security_notes.md"
    sample.write_text("notes")

    status = importer.import_file(sample)
    assert status == ScanStatus.clean
    resources = repo.list_resources(limit=5)
    assert resources
