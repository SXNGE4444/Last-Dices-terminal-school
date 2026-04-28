from last_dices_terminal_school.agents.hub import AgentHub
from last_dices_terminal_school.ai.service import AIService


def test_agent_hub_safe_default_provider() -> None:
    hub = AgentHub(AIService())
    response = hub.for_lesson("Linux shell survival", weak_areas="permissions")

    assert response.agent_name == "study_coach"
    assert response.summary
    assert response.safety_notes
