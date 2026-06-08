from pprint import pprint

from orchestrator.answer_aggregator import (
    answer_aggregator_node,
)

from schemas.normalized_agent_response import (
    NormalizedAgentResponse,
)

from schemas.answer_type import (
    AnswerType,
)

state = {

    "classified_responses": [

        NormalizedAgentResponse(

            source="servicenow",

            answer=
                "Integration latency is causing PTO failures.",

            answer_type=
                AnswerType.ROOT_CAUSE,
        )
    ]
}

result = answer_aggregator_node(
    state
)

pprint(
    result[
        "aggregated_answers"
    ].model_dump()
)