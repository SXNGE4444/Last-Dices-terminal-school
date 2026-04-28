from pathlib import Path

from watchdog.events import FileSystemEventHandler

from last_dices_terminal_school.services.material_import_service import MaterialImportService


class IngestionHandler(FileSystemEventHandler):
    def __init__(self, importer: MaterialImportService):
        super().__init__()
        self.importer = importer

    def on_created(self, event):  # type: ignore[override]
        if event.is_directory:
            return
        self.importer.import_file(Path(event.src_path))
