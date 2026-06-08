from pprint import pprint

from orchestrator.answer_synthesizer import (
    answer_synthesizer_node,
)

from schemas.normalized_agent_response import (
    NormalizedAgentResponse,
)

from schemas.answer_type import (
    AnswerType,
)

from schemas.conflict_analysis import (
    ConflictAnalysis,
)

from schemas.aggregated_answers import (
    AggregatedAnswers,
)


state = {

    "query":
        "Why are PTO approvals failing?",

    "aggregated_answers":

        AggregatedAnswers(

            primary_answer=

                NormalizedAgentResponse(

                    source="servicenow",

                    answer=(
                        "PTO approvals are failing "
                        "due to integration latency."
                    ),

                    answer_type=
                        AnswerType.ROOT_CAUSE,
                ),

            supporting_answers=[

                NormalizedAgentResponse(

                    source="confluence",

                    answer=(
                        "PTO approvals are processed "
                        "through Workday."
                    ),

                    answer_type=
                        AnswerType.PROCESS,
                ),

                NormalizedAgentResponse(

                    source="barnum",

                    answer=(
                        "Community users reported "
                        "intermittent approval delays."
                    ),

                    answer_type=
                        AnswerType.OBSERVATION,
                ),
            ],

            conflict_analysis=

                ConflictAnalysis(

                    conflict_detected=
                        False,

                    consensus_score=
                        1.0,

                    confidence_score=
                        0.88,

                    minimum_similarity=
                        1.0,

                    average_similarity=
                        1.0,
                ),
        )
}

result = answer_synthesizer_node(
    state
)

print("\n")
print("=" * 100)
print("FINAL ANSWER")
print("=" * 100)

pprint(
    result[
        "final_answer"
    ].model_dump()
)

print("\n")
print("=" * 100)
print("EXECUTION TRACE")
print("=" * 100)

for event in result[
    "execution_trace"
]:

    pprint(
        event.model_dump()
    )