from last_dices_terminal_school.core.models import Quiz


class QuizEngine:
    @staticmethod
    def grade(quiz: Quiz, answers: list[int]) -> float:
        if not quiz.questions:
            return 0.0

        correct = 0
        for idx, question in enumerate(quiz.questions):
            if idx < len(answers) and answers[idx] == question.answer_index:
                correct += 1
        return round((correct / len(quiz.questions)) * 100.0, 2)
