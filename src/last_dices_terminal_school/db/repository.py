from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

from last_dices_terminal_school.core.models import Assignment, Goal, Quiz, Task


class SchoolRepository:
    def __init__(self, db_path: Path):
        self.db_path = db_path

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def save_lessons(self, lessons: list[dict[str, Any]]) -> None:
        with self._connect() as conn:
            conn.executemany(
                """INSERT OR REPLACE INTO lessons (id, year, track, title, objective, estimated_minutes)
                VALUES (:id, :year, :track, :title, :objective, :estimated_minutes)""",
                lessons,
            )
            conn.commit()

    def save_tasks(self, tasks: list[Task]) -> None:
        with self._connect() as conn:
            conn.executemany(
                "INSERT OR REPLACE INTO tasks (id, lesson_id, title, status) VALUES (?, ?, ?, ?)",
                [(t.id, t.lesson_id, t.title, t.status) for t in tasks],
            )
            conn.commit()

    def save_goals(self, goals: list[Goal]) -> None:
        with self._connect() as conn:
            conn.executemany(
                "INSERT OR REPLACE INTO goals (id, scope, title, target_value) VALUES (?, ?, ?, ?)",
                [(g.id, g.scope, g.title, g.target_value) for g in goals],
            )
            conn.commit()

    def save_assignments(self, assignments: list[Assignment]) -> None:
        with self._connect() as conn:
            conn.executemany(
                "INSERT OR REPLACE INTO assignments (id, lesson_id, title, prompt, rubric_json) VALUES (?, ?, ?, ?, ?)",
                [(a.id, a.lesson_id, a.title, a.prompt, json.dumps(a.rubric)) for a in assignments],
            )
            conn.commit()

    def save_quizzes(self, quizzes: list[Quiz]) -> None:
        with self._connect() as conn:
            conn.executemany(
                "INSERT OR REPLACE INTO quizzes (id, lesson_id, title, questions_json) VALUES (?, ?, ?, ?)",
                [(q.id, q.lesson_id, q.title, q.model_dump_json()) for q in quizzes],
            )
            conn.commit()

    def save_scenarios(self, scenarios: list[dict[str, str]]) -> None:
        normalized: list[dict[str, str]] = []
        for scenario in scenarios:
            normalized.append(
                {
                    "id": scenario["id"],
                    "title": scenario["title"],
                    "focus": scenario.get("focus") or scenario.get("severity", "general"),
                }
            )

        with self._connect() as conn:
            conn.executemany(
                "INSERT OR REPLACE INTO scenarios (id, title, focus) VALUES (:id, :title, :focus)",
                normalized,
            )
            conn.commit()

    def save_report(self, title: str, body: str) -> None:
        with self._connect() as conn:
            conn.execute("INSERT INTO reports (title, body) VALUES (?, ?)", (title, body))
            conn.commit()

    def save_scan_log(self, file_path: str, status: str, details: str, signature: str | None = None) -> None:
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO import_scans (file_path, status, details, signature) VALUES (?, ?, ?, ?)",
                (file_path, status, details, signature),
            )
            conn.commit()

    def index_material(
        self,
        file_path: str,
        file_name: str,
        extension: str,
        size_bytes: int,
        sha256: str,
        topics: list[str],
        status: str,
    ) -> None:
        with self._connect() as conn:
            conn.execute(
                """INSERT OR REPLACE INTO material_library
                (file_path, file_name, extension, size_bytes, sha256, topics_json, status)
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (file_path, file_name, extension, size_bytes, sha256, json.dumps(topics), status),
            )
            conn.commit()

    def list_resources(self, limit: int = 8) -> list[tuple[str, str]]:
        with self._connect() as conn:
            return conn.execute(
                "SELECT file_path, status FROM material_library ORDER BY indexed_at DESC LIMIT ?",
                (limit,),
            ).fetchall()

    def latest_scan_logs(self, limit: int = 10) -> list[tuple[str, str, str]]:
        with self._connect() as conn:
            return conn.execute(
                "SELECT file_path, status, logged_at FROM import_scans ORDER BY logged_at DESC LIMIT ?",
                (limit,),
            ).fetchall()

    def list_lessons(self, limit: int = 8) -> list[tuple[str, str, int]]:
        with self._connect() as conn:
            return conn.execute(
                "SELECT id, title, year FROM lessons ORDER BY year, id LIMIT ?", (limit,)
            ).fetchall()

    def list_assignments(self, limit: int = 6) -> list[tuple[str, str]]:
        with self._connect() as conn:
            return conn.execute("SELECT id, title FROM assignments ORDER BY id LIMIT ?", (limit,)).fetchall()

    def list_quizzes(self, limit: int = 6) -> list[tuple[str, str]]:
        with self._connect() as conn:
            return conn.execute("SELECT id, title FROM quizzes ORDER BY id LIMIT ?", (limit,)).fetchall()

    def latest_reports(self, limit: int = 4) -> list[tuple[str, str]]:
        with self._connect() as conn:
            return conn.execute(
                "SELECT title, created_at FROM reports ORDER BY created_at DESC LIMIT ?", (limit,)
            ).fetchall()


    def record_quiz_attempt(
        self,
        quiz_id: str,
        lesson_id: str,
        module_id: str,
        domain: str,
        score: float,
        passed: bool,
        answers: list[int],
    ) -> None:
        with self._connect() as conn:
            conn.execute(
                """INSERT INTO quiz_attempts
                (quiz_id, lesson_id, module_id, domain, score, passed, answers_json)
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (quiz_id, lesson_id, module_id, domain, score, int(passed), json.dumps(answers)),
            )
            conn.commit()

    def quiz_score_history(self, quiz_id: str) -> list[tuple[float, str]]:
        with self._connect() as conn:
            return conn.execute(
                "SELECT score, attempted_at FROM quiz_attempts WHERE quiz_id = ? ORDER BY id DESC",
                (quiz_id,),
            ).fetchall()

    def weak_domains(self) -> list[tuple[str, float, int]]:
        with self._connect() as conn:
            return conn.execute(
                """SELECT domain, AVG(score) as avg_score, COUNT(*) as attempts
                FROM quiz_attempts GROUP BY domain ORDER BY avg_score ASC"""
            ).fetchall()

    def save_assignment_submission(
        self,
        assignment_id: str,
        module_id: str,
        scenario_id: str | None,
        content: str,
        notes_path: str | None,
        feedback_json: str,
        dimensions_json: str,
        total_score: float,
        improved_from_submission_id: int | None,
    ) -> int:
        with self._connect() as conn:
            cur = conn.execute(
                """INSERT INTO assignment_submissions
                (assignment_id, module_id, scenario_id, content, notes_path, feedback_json, dimensions_json,
                 total_score, improved_from_submission_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    assignment_id,
                    module_id,
                    scenario_id,
                    content,
                    notes_path,
                    feedback_json,
                    dimensions_json,
                    total_score,
                    improved_from_submission_id,
                ),
            )
            conn.commit()
            return int(cur.lastrowid)

    def assignment_history(self, assignment_id: str) -> list[tuple[float, str]]:
        with self._connect() as conn:
            return conn.execute(
                "SELECT total_score, submitted_at FROM assignment_submissions WHERE assignment_id = ? ORDER BY id DESC",
                (assignment_id,),
            ).fetchall()

    def add_progress_event(self, event_type: str, lesson_id: str | None, module_id: str | None, details_json: str) -> None:
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO progress_events (event_type, lesson_id, module_id, details_json) VALUES (?, ?, ?, ?)",
                (event_type, lesson_id, module_id, details_json),
            )
            conn.commit()

    def progress_summary(self) -> dict[str, int]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT event_type, COUNT(*) FROM progress_events GROUP BY event_type"
            ).fetchall()
        return {event_type: count for event_type, count in rows}

    def dashboard_snapshot(self) -> dict[str, Any]:
        with self._connect() as conn:
            today_lesson = conn.execute("SELECT title, track FROM lessons ORDER BY year, id LIMIT 1").fetchone()
            lesson_count = conn.execute("SELECT COUNT(*) FROM lessons").fetchone()[0]
            task_done = conn.execute("SELECT COUNT(*) FROM tasks WHERE status = 'done'").fetchone()[0]
            task_total = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
            submission_count = conn.execute("SELECT COUNT(*) FROM submissions").fetchone()[0]
            profile = conn.execute("SELECT learner_name, specialization_track FROM learner_profile WHERE id = 1").fetchone()

            weekly_goals = [row[0] for row in conn.execute("SELECT title FROM goals WHERE scope = 'weekly' ORDER BY id LIMIT 3").fetchall()]
            monthly_goals = [row[0] for row in conn.execute("SELECT title FROM goals WHERE scope = 'monthly' ORDER BY id LIMIT 3").fetchall()]

        completion_base = (submission_count * 4) + task_done
        completion_total = max(1, (task_total + 40))
        progress = min(100.0, (completion_base / completion_total) * 100)
        return {
            "learner_name": profile[0] if profile else "Learner",
            "specialization_track": profile[1] if profile else "Year 1 Foundations",
            "today_lesson": today_lesson[0] if today_lesson else "No lesson loaded",
            "today_track": today_lesson[1] if today_lesson else "N/A",
            "weekly_goals": weekly_goals or ["Complete 5 lessons", "Submit 2 assignments"],
            "monthly_goals": monthly_goals or ["Finish current module", "Run 2 scenario drills"],
            "overall_progress": progress,
            "lesson_count": lesson_count,
            "task_done": task_done,
            "task_total": task_total,
        }
