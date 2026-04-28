from __future__ import annotations

from datetime import datetime
from enum import Enum
from pathlib import Path

from pydantic import BaseModel, Field


class ScanStatus(str, Enum):
    pending = "pending"
    scanning = "scanning"
    clean = "clean"
    quarantined = "quarantined"
    failed = "failed"


class FileTopic(str, Enum):
    linux = "linux"
    networking = "networking"
    security = "security"
    logistics = "logistics"
    maritime = "maritime"
    supply_chain = "supply-chain"
    ai = "AI"
    python = "Python"
    general = "general"


class ScanResultModel(BaseModel):
    file_path: Path
    status: ScanStatus
    details: str
    scanned_at: datetime = Field(default_factory=datetime.utcnow)
    signature: str | None = None


class MaterialRecord(BaseModel):
    file_path: Path
    file_name: str
    extension: str
    size_bytes: int
    sha256: str
    topics: list[FileTopic]
    status: ScanStatus
    indexed_at: datetime = Field(default_factory=datetime.utcnow)
