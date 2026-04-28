from pathlib import Path

from pydantic import BaseModel


class AppSettings(BaseModel):
    app_name: str = "LAST DICES // TERMINAL SCHOOL OS"
    data_root: Path = Path.home() / ".last_dices_terminal_school"
    db_path: Path = Path.home() / ".last_dices_terminal_school" / "school.db"
    import_dir: Path = Path("import_materials")
    quarantine_dir: Path = Path("quarantine")
    scans_dir: Path = Path("logs/scans")
    curriculum_file: Path = Path("data/curriculum/curriculum.yaml")
    scenario_file: Path = Path("data/scenarios/scenarios.yaml")


settings = AppSettings()
settings.data_root.mkdir(parents=True, exist_ok=True)
settings.import_dir.mkdir(parents=True, exist_ok=True)
settings.quarantine_dir.mkdir(parents=True, exist_ok=True)
settings.scans_dir.mkdir(parents=True, exist_ok=True)
