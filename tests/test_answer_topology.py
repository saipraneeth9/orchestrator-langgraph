from pprint import pprint

from orchestrator.answer_topology import (
    answer_topology_node,
)

from schemas.answer_type import (
    AnswerType,
)

from schemas.normalized_agent_response import (
    NormalizedAgentResponse,
)

from schemas.aggregated_answers import (
    AggregatedAnswers,
)

from schemas.conflict_analysis import (
    ConflictAnalysis,
)


state = {

    "classified_responses": [

        NormalizedAgentResponse(

            source="servicenow",

            answer="Latency issue",

            answer_type=
                AnswerType
                .ROOT_CAUSE,
        ),

        NormalizedAgentResponse(

            source="confluence",

            answer="Workflow process",

            answer_type=
                AnswerType
                .PROCESS,
        ),

        NormalizedAgentResponse(

            source="sharepoint",

            answer="PTO policy",

            answer_type=
                AnswerType
                .POLICY,
        ),
    ],

    "aggregated_answers":

        AggregatedAnswers(

            primary_answer=

                NormalizedAgentResponse(

                    source="servicenow",

                    answer="Latency issue",
                ),

            supporting_answers=[],

            conflict_analysis=

                ConflictAnalysis(

                    conflict_detected=
                        False,

                    consensus_score=
                        1.0,

                    minimum_similarity=
                        1.0,

                    average_similarity=
                        1.0,

                    confidence_score=
                        0.95,
                )
        )
}

result = answer_topology_node(
    state
)

print("\n")
print("=" * 100)
print("ANSWER TOPOLOGY")
print("=" * 100)

pprint(
    result[
        "answer_topology"
    ].model_dump()
)