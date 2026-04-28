from last_dices_terminal_school.engines.assignment_engine import AssignmentEngine


def test_assignment_marking() -> None:
    feedback = AssignmentEngine.mark("This is a defensive write-up with controls and detection steps.")
    assert feedback.marker_agent == "assignment_marker"
    assert feedback.score >= 40
