from pathlib import Path

from last_dices_terminal_school.core.settings import REPO_ROOT, settings


def test_default_storage_paths_are_repo_local():
    assert settings.storage_root == REPO_ROOT / "storage"
    assert settings.db_path == REPO_ROOT / "storage" / "school.db"
    assert settings.import_dir == REPO_ROOT / "storage" / "import_materials"
    assert settings.quarantine_dir == REPO_ROOT / "storage" / "quarantine"
    assert settings.scans_dir == REPO_ROOT / "storage" / "logs" / "scans"

    assert Path(settings.import_dir).exists()
    assert Path(settings.quarantine_dir).exists()
    assert Path(settings.scans_dir).exists()
