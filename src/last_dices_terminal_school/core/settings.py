from __future__ import annotations

import os
from pathlib import Path

from pydantic import BaseModel


REPO_ROOT = Path(__file__).resolve().parents[3]


class AppSettings(BaseModel):
    app_name: str = "LAST DICES // TERMINAL SCHOOL OS"

    repo_root: Path = Path(os.getenv("LDTS_REPO_ROOT", REPO_ROOT))
    storage_root: Path = Path(os.getenv("LDTS_STORAGE_ROOT", REPO_ROOT / "storage"))

    data_root: Path = Path(os.getenv("LDTS_DATA_ROOT", REPO_ROOT / "data"))
    db_path: Path = Path(os.getenv("LDTS_DB_PATH", REPO_ROOT / "storage" / "school.db"))

    import_dir: Path = Path(os.getenv("LDTS_IMPORT_DIR", REPO_ROOT / "storage" / "import_materials"))
    quarantine_dir: Path = Path(os.getenv("LDTS_QUARANTINE_DIR", REPO_ROOT / "storage" / "quarantine"))
    scans_dir: Path = Path(os.getenv("LDTS_SCANS_DIR", REPO_ROOT / "storage" / "logs" / "scans"))

    curriculum_file: Path = Path(os.getenv("LDTS_CURRICULUM_FILE", REPO_ROOT / "data" / "curriculum" / "curriculum.yaml"))
    scenario_file: Path = Path(os.getenv("LDTS_SCENARIO_FILE", REPO_ROOT / "data" / "scenarios" / "scenarios.yaml"))


settings = AppSettings()
settings.storage_root.mkdir(parents=True, exist_ok=True)
settings.import_dir.mkdir(parents=True, exist_ok=True)
settings.quarantine_dir.mkdir(parents=True, exist_ok=True)
settings.scans_dir.mkdir(parents=True, exist_ok=True)
