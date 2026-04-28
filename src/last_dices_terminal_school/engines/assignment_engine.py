from last_dices_terminal_school.core.models import Feedback


class AssignmentEngine:
    @staticmethod
    def mark(content: str) -> Feedback:
        word_count = len(content.split())
        base = min(100, 40 + word_count * 0.3)
        strengths = [
            "Clear defensive focus",
            "Good structure",
        ]
        improvements = [
            "Add more logistics-specific controls",
            "Reference detection and response metrics",
        ]
        return Feedback(
            score=round(base, 2),
            strengths=strengths,
            improvements=improvements,
            marker_agent="assignment_marker",
        )
