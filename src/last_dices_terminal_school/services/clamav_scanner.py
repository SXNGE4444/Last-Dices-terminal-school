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
        if shutil.which("clamscan") is None:
            return self._log(file_path, ScanStatus.failed, "clamscan missing")

        try:
            proc = subprocess.run(
                ["clamscan", str(file_path)],
                capture_output=True,
                text=True,
                timeout=30,
            )
        except subprocess.TimeoutExpired:
            return self._log(file_path, ScanStatus.failed, "clamscan timeout")

        output = ((proc.stdout or "") + (proc.stderr or "")).strip()
        signature = self._extract_signature(output)

        if proc.returncode == 0:
            return self._log(file_path, ScanStatus.clean, "no threats detected", None)

        if proc.returncode == 1:
            destination = self.quarantine_dir / file_path.name
            if file_path.exists():
                shutil.move(str(file_path), str(destination))
            return self._log(file_path, ScanStatus.quarantined, output or "infected", signature)

        # returncode == 2 or other scanner failure states
        return self._log(file_path, ScanStatus.failed, output or "clamscan scan failure", signature)

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

    def _log(
        self,
        file_path: Path,
        status: ScanStatus,
        details: str,
        signature: str | None = None,
    ) -> ScanResultModel:
        result = ScanResultModel(
            file_path=file_path,
            status=status,
            details=details,
            signature=signature,
        )
        self._write_log(result)
        return result
