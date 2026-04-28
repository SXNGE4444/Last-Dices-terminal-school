from __future__ import annotations

from pathlib import Path

import yaml

from last_dices_terminal_school.core.school_models import ObjectiveQuestion, QuizAttemptModel
from last_dices_terminal_school.db.repository import SchoolRepository


class QuizService:
    def __init__(self, repo: SchoolRepository, quiz_bank_path: Path):
        self.repo = repo
        data = yaml.safe_load(quiz_bank_path.read_text())
        self.questions = [ObjectiveQuestion(**q) for q in data.get("questions", [])]

    def questions_for_quiz(self, quiz_id: str) -> list[ObjectiveQuestion]:
        return [q for q in self.questions if q.quiz_id == quiz_id]

    def attempt_quiz(self, quiz_id: str, answers: list[int]) -> QuizAttemptModel:
        qs = self.questions_for_quiz(quiz_id)
        if not qs:
            raise ValueError(f"Unknown quiz: {quiz_id}")

        correct = 0
        explanations = []
        for i, q in enumerate(qs):
            user = answers[i] if i < len(answers) else -1
            if user == q.answer_index:
                correct += 1
                explanations.append(f"Q{i+1} correct: {q.explanation}")
            else:
                explanations.append(f"Q{i+1} review: {q.explanation}")

        score = round((correct / len(qs)) * 100, 2)
        passed = score >= 70
        first = qs[0]

        attempt = QuizAttemptModel(
            quiz_id=quiz_id,
            lesson_id=first.lesson_id,
            module_id=first.module_id,
            domain=first.domain,
            answers=answers,
            score=score,
            passed=passed,
            explanations=explanations,
        )
        self.repo.record_quiz_attempt(
            quiz_id=attempt.quiz_id,
            lesson_id=attempt.lesson_id,
            module_id=attempt.module_id,
            domain=attempt.domain,
            score=attempt.score,
            passed=attempt.passed,
            answers=attempt.answers,
        )
        return attempt

    def weak_domain_tracking(self) -> list[dict[str, str]]:
        rows = self.repo.weak_domains()
        findings = []
        for domain, avg, attempts in rows:
            level = "high" if avg < 70 else "medium" if avg < 80 else "ok"
            findings.append(
                {
                    "domain": domain,
                    "average": f"{avg:.1f}",
                    "attempts": str(attempts),
                    "risk": level,
                }
            )
        return findings

    def score_history(self, quiz_id: str) -> list[tuple[float, str]]:
        return self.repo.quiz_score_history(quiz_id)
