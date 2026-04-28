from __future__ import annotations

import time

from watchdog.observers import Observer

from last_dices_terminal_school.core.settings import settings
from last_dices_terminal_school.db.repository import SchoolRepository
from last_dices_terminal_school.db.schema import init_db
from last_dices_terminal_school.services.clamav_scanner import ClamAVScanner
from last_dices_terminal_school.services.file_ingestion import IngestionHandler
from last_dices_terminal_school.services.material_import_service import MaterialImportService


def main() -> None:
    init_db(settings.db_path)
    repo = SchoolRepository(settings.db_path)
    scanner = ClamAVScanner(settings.quarantine_dir, settings.scans_dir)
    importer = MaterialImportService(repo, scanner)

    handler = IngestionHandler(importer)
    observer = Observer()
    observer.schedule(handler, str(settings.import_dir), recursive=True)
    observer.start()
    print(f"[LAST DICES] Watching imports: {settings.import_dir.resolve()}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[LAST DICES] Watcher stopped")
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    main()
