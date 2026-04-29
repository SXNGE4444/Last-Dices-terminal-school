import sqlite3
from pathlib import Path


DDL_STATEMENTS = [
    """
    CREATE TABLE IF NOT EXISTS learner_profile (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        learner_name TEXT NOT NULL DEFAULT 'Learner',
        specialization_track TEXT NOT NULL DEFAULT 'Year 1 Foundations',
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS lessons (
        id TEXT PRIMARY KEY,
        year INTEGER NOT NULL,
        track TEXT NOT NULL,
        title TEXT NOT NULL,
        objective TEXT NOT NULL,
        estimated_minutes INTEGER NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS tasks (
        id TEXT PRIMARY KEY,
        lesson_id TEXT NOT NULL,
        title TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (lesson_id) REFERENCES lessons(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS goals (
        id TEXT PRIMARY KEY,
        scope TEXT NOT NULL,
        title TEXT NOT NULL,
        target_value INTEGER NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS assignments (
        id TEXT PRIMARY KEY,
        lesson_id TEXT NOT NULL,
        title TEXT NOT NULL,
        prompt TEXT NOT NULL,
        rubric_json TEXT NOT NULL,
        FOREIGN KEY (lesson_id) REFERENCES lessons(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS quizzes (
        id TEXT PRIMARY KEY,
        lesson_id TEXT NOT NULL,
        title TEXT NOT NULL,
        questions_json TEXT NOT NULL,
        FOREIGN KEY (lesson_id) REFERENCES lessons(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        assignment_id TEXT NOT NULL,
        content TEXT NOT NULL,
        score REAL,
        feedback_json TEXT,
        submitted_on TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (assignment_id) REFERENCES assignments(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS material_library (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_path TEXT NOT NULL UNIQUE,
        file_name TEXT NOT NULL,
        extension TEXT NOT NULL,
        size_bytes INTEGER NOT NULL,
        sha256 TEXT NOT NULL,
        topics_json TEXT NOT NULL,
        status TEXT NOT NULL,
        indexed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS import_scans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_path TEXT NOT NULL,
        status TEXT NOT NULL,
        details TEXT NOT NULL,
        signature TEXT,
        logged_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS scenarios (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        focus TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS quiz_attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quiz_id TEXT NOT NULL,
        lesson_id TEXT,
        module_id TEXT,
        domain TEXT NOT NULL,
        score REAL NOT NULL,
        passed INTEGER NOT NULL,
        answers_json TEXT NOT NULL,
        attempted_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS assignment_submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        assignment_id TEXT NOT NULL,
        module_id TEXT,
        scenario_id TEXT,
        content TEXT NOT NULL,
        notes_path TEXT,
        feedback_json TEXT NOT NULL,
        dimensions_json TEXT NOT NULL,
        total_score REAL NOT NULL,
        improved_from_submission_id INTEGER,
        submitted_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS progress_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_type TEXT NOT NULL,
        lesson_id TEXT,
        module_id TEXT,
        details_json TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        body TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """,
]


def init_db(db_path: Path) -> None:
    with sqlite3.connect(db_path) as conn:
        for stmt in DDL_STATEMENTS:
            conn.execute(stmt)

        conn.execute(
            "INSERT OR IGNORE INTO learner_profile (id, learner_name, specialization_track) VALUES (1, 'Learner', 'Year 1 Foundations')"
        )
        conn.commit()
