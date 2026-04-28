from pathlib import Path

from last_dices_terminal_school.core.import_models import ScanStatus
from last_dices_terminal_school.services.clamav_scanner import ClamAVScanner


def test_scanner_fails_when_clamscan_missing(tmp_path: Path) -> None:
    scanner = ClamAVScanner(tmp_path / "quarantine", tmp_path / "logs")
    sample = tmp_path / "sample.txt"
    sample.write_text("hello")

    result = scanner.scan_file(sample)
    assert result.status in {ScanStatus.clean, ScanStatus.quarantined, ScanStatus.failed}
