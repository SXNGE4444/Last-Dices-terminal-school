from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from last_dices_terminal_school.core.import_models import ScanResultModel, ScanStatus


class ClamAVScanner:
    def __init__(self, quarantine_dir: Path, scans_dir: Path):
        self.quarantine_dir = quarantine_dir
        self.scans_dir = scans_dir
        self.quarantine_dir.mkdir(parents=True, exist_ok=True)
        self.scans_dir.mkdir(parents=True, exist_ok=True)

    def scan_file(self, file_path: Path) -> ScanResultModel:
        if not file_path.exists():
            result = ScanResultModel(file_path=file_path, status=ScanStatus.failed, details="file missing")
            self._write_log(result)
            return result

        if shutil.which("clamscan") is None:
            result = ScanResultModel(
                file_path=file_path,
                status=ScanStatus.failed,
                details="clamscan not found",
            )
            self._write_log(result)
            return result

        run = subprocess.run(
            ["clamscan", "--no-summary", str(file_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        output = (run.stdout or run.stderr).strip()

        if run.returncode == 0 and "OK" in output:
            result = ScanResultModel(file_path=file_path, status=ScanStatus.clean, details=output)
            self._write_log(result)
            return result

        signature = self._extract_signature(output)
        quarantine_path = self.quarantine_dir / file_path.name
        file_path.replace(quarantine_path)
        result = ScanResultModel(
            file_path=quarantine_path,
            status=ScanStatus.quarantined,
            details=output or "infected or suspicious",
            signature=signature,
        )
        self._write_log(result)
        return result

    def _extract_signature(self, output: str) -> str | None:
        if "FOUND" in output:
            return output.split("FOUND")[0].split(":")[-1].strip() or "detected"
        return None

    def _write_log(self, result: ScanResultModel) -> None:
        log_file = self.scans_dir / "scan.log"
        with log_file.open("a", encoding="utf-8") as f:
            f.write(
                f"{result.scanned_at.isoformat()} | {result.status.value} | {result.file_path} | {result.details}\n"
            )
