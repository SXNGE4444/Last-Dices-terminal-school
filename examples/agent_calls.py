from pathlib import Path

from last_dices_terminal_school.agents.hub import AgentHub
from last_dices_terminal_school.ai.contracts import AgentRequest
from last_dices_terminal_school.ai.service import AIService
from last_dices_terminal_school.services.ai_pathway_service import AIPathwayService


def main() -> None:
    hub = AgentHub(AIService())  # NullProvider safe default
    ai_pathway = AIPathwayService(Path("data/ai_pathway/modules.yaml"), Path("data/ai_pathway/project_ladder.yaml"))

    lesson_plan = hub.for_lesson("Linux shell survival", weak_areas="permissions and segmentation")
    print("\n[Study Coach]\n", lesson_plan.summary)

    quiz_help = hub.for_quiz_review("Ports, protocols, and segmentation for warehouse defense")
    print("\n[Quiz Master]\n", quiz_help.summary)

    feedback = hub.for_assignment_feedback("I propose detect and contain steps for logistics incidents.")
    print("\n[Assignment Marker]\n", feedback.summary)

    reflection = hub.for_scenario_reflection("shipping manifest tampering")
    print("\n[Red Blue Reflector]\n", reflection.summary)

    ai_build = hub.run(
        AgentRequest(
            agent_name="ai_builder",
            objective="AI engineering roadmap",
            context=ai_pathway.ai_builder_context(),
        )
    )
    print("\n[AI Builder]\n", ai_build.summary)


if __name__ == "__main__":
    main()
