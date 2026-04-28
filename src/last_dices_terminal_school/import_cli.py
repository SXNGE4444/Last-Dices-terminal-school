from pathlib import Path

from last_dices_terminal_school.core.settings import settings
from last_dices_terminal_school.db.repository import SchoolRepository
from last_dices_terminal_school.db.schema import init_db
from last_dices_terminal_school.services.clamav_scanner import ClamAVScanner
from last_dices_terminal_school.services.material_import_service import MaterialImportService


def main() -> None:
    init_db(settings.db_path)
    repo = SchoolRepository(settings.db_path)
    scanner = ClamAVScanner(settings.quarantine_dir, settings.scans_dir)
    importer = MaterialImportService(repo, scanner)

    counts = importer.scan_folder(Path(settings.import_dir))
    print("[LAST DICES] folder scan complete")
    for k, v in counts.items():
        print(f"- {k}: {v}")


if __name__ == "__main__":
    main()
