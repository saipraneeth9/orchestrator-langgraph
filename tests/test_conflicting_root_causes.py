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
                "PTO approvals fail due to integration latency.",

            answer_type=
                AnswerType.ROOT_CAUSE,
        ),

        NormalizedAgentResponse(

            source="confluence",

            answer=
                "PTO approvals fail because the database is unavailable.",

            answer_type=
                AnswerType.ROOT_CAUSE,
        ),
    ]
}

result = answer_aggregator_node(
    state
)

print("\n")
print("=" * 100)
print("CONFLICT ANALYSIS")
print("=" * 100)

pprint(

    result[
        "aggregated_answers"
    ]
    .conflict_analysis
    .model_dump()

)