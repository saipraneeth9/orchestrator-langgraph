from pprint import pprint

from orchestrator.conflict_resolution import (
    conflict_resolution_node,
)

from schemas.aggregated_answers import (
    AggregatedAnswers,
)

from schemas.conflict_analysis import (
    ConflictAnalysis,
)

from schemas.normalized_agent_response import (
    NormalizedAgentResponse,
)

from schemas.source_trust import (
    SourceTrust,
)

state = {

    "aggregated_answers":

        AggregatedAnswers(

            primary_answer=

                NormalizedAgentResponse(

                    source="servicenow",

                    answer=(
                        "PTO approvals are failing "
                        "due to integration latency."
                    ),
                ),

            supporting_answers=[

                NormalizedAgentResponse(

                    source="confluence",

                    answer=(
                        "PTO approvals are failing "
                        "due to permission issues."
                    ),
                ),

                NormalizedAgentResponse(

                    source="barnum",

                    answer=(
                        "PTO approvals are failing "
                        "due to token expiry."
                    ),
                ),
            ],

            conflict_analysis=

                ConflictAnalysis(

                    conflict_detected=True,

                    consensus_score=0.45,

                    minimum_similarity=0.40,

                    average_similarity=0.45,

                    confidence_score=0.42,
                ),
        ),

    "source_trust": [

        SourceTrust(

            source="servicenow",

            base_authority=1.0,

            evidence_strength=1.0,

            source_type_confidence=1.0,

            coverage_score=1.0,

            trust_score=1.0,
        ),

        SourceTrust(

            source="confluence",

            base_authority=0.95,

            evidence_strength=1.0,

            source_type_confidence=0.95,

            coverage_score=1.0,

            trust_score=0.95,
        ),

        SourceTrust(

            source="barnum",

            base_authority=0.70,

            evidence_strength=1.0,

            source_type_confidence=0.70,

            coverage_score=1.0,

            trust_score=0.70,
        ),
    ],
}

result = conflict_resolution_node(
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