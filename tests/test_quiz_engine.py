from last_dices_terminal_school.core.models import Quiz, QuizQuestion
from last_dices_terminal_school.engines.quiz_engine import QuizEngine


def test_grade_quiz() -> None:
    quiz = Quiz(
        id="q1",
        lesson_id="l1",
        title="t",
        questions=[
            QuizQuestion(question="a", choices=["1", "2"], answer_index=0),
            QuizQuestion(question="b", choices=["1", "2"], answer_index=1),
        ],
    )

    assert QuizEngine.grade(quiz, [0, 1]) == 100.0
    assert QuizEngine.grade(quiz, [0, 0]) == 50.0
