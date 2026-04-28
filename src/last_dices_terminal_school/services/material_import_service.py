from __future__ import annotations

import hashlib
from pathlib import Path

from last_dices_terminal_school.core.import_models import FileTopic, ScanStatus
from last_dices_terminal_school.db.repository import SchoolRepository
from last_dices_terminal_school.services.clamav_scanner import ClamAVScanner


SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md", ".docx", ".zip"}


class MaterialImportService:
    def __init__(self, repo: SchoolRepository, scanner: ClamAVScanner):
        self.repo = repo
        self.scanner = scanner

    def import_file(self, file_path: Path) -> ScanStatus:
        if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            self.repo.save_scan_log(str(file_path), ScanStatus.failed.value, "unsupported extension")
            return ScanStatus.failed

        self.repo.save_scan_log(str(file_path), ScanStatus.pending.value, "queued for scanning")
        self.repo.save_scan_log(str(file_path), ScanStatus.scanning.value, "running clamav scan")
        result = self.scanner.scan_file(file_path)
        self.repo.save_scan_log(
            str(result.file_path),
            result.status.value,
            result.details,
            result.signature,
        )

        if result.status == ScanStatus.clean:
            self._index_clean_file(result.file_path)
        return result.status

    def scan_folder(self, folder: Path) -> dict[str, int]:
        counts = {k.value: 0 for k in ScanStatus}
        for path in folder.glob("**/*"):
            if path.is_file():
                status = self.import_file(path)
                counts[status.value] += 1
        return counts

    def _index_clean_file(self, file_path: Path) -> None:
        sha256 = self._hash_file(file_path)
        topics = [t.value for t in self._infer_topics(file_path.name)]
        size = file_path.stat().st_size

        self.repo.index_material(
            file_path=str(file_path),
            file_name=file_path.name,
            extension=file_path.suffix.lower(),
            size_bytes=size,
            sha256=sha256,
            topics=topics,
            status=ScanStatus.clean.value,
        )

    @staticmethod
    def _hash_file(file_path: Path) -> str:
        h = hashlib.sha256()
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()

    @staticmethod
    def _infer_topics(name: str) -> list[FileTopic]:
        text = name.lower()
        mapping = {
            "linux": FileTopic.linux,
            "network": FileTopic.networking,
            "security": FileTopic.security,
            "logistics": FileTopic.logistics,
            "maritime": FileTopic.maritime,
            "supply": FileTopic.supply_chain,
            "ai": FileTopic.ai,
            "python": FileTopic.python,
        }
        topics = [v for k, v in mapping.items() if k in text]
        return topics or [FileTopic.general]
