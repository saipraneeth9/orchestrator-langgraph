from pprint import pprint

from schemas.source_trust import (
    SourceTrust,
)

from orchestrator.strategy_router import (
    strategy_router,
)

from orchestrator.direct_response import (
    direct_response_node,
)

from orchestrator.low_confidence import (
    low_confidence_node,
)

from schemas.response_strategy import (
    ResponseStrategy,
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


def run_direct_response():

    print("\n")
    print("=" * 100)
    print("DIRECT RESPONSE")
    print("=" * 100)

    state = {

    "response_strategy":
        ResponseStrategy.DIRECT_RESPONSE,

    "aggregated_answers":

        AggregatedAnswers(

            primary_answer=

                NormalizedAgentResponse(

                    source="servicenow",

                    answer=(
                        "Integration latency "
                        "caused PTO failures."
                    ),
                ),

            supporting_answers=[],

            conflict_analysis=

                ConflictAnalysis(

                    conflict_detected=False,

                    consensus_score=1.0,

                    minimum_similarity=1.0,

                    average_similarity=1.0,

                    confidence_score=1.0,
                ),
        ),

    "source_trust": [

        SourceTrust(

            source="servicenow",

            base_authority=1.0,

            evidence_strength=0.0,

            source_type_confidence=1.0,

            coverage_score=0.0,

            trust_score=0.85,

            performance_score=0.87,

            effective_trust=0.86,

            trust_rank=1,

            trust_tier="HIGH",
        )
    ],
}
    route = strategy_router(
        state
    )

    print(
        f"Route: {route}"
    )

    result = direct_response_node(
        state
    )

    pprint(
        result[
            "final_answer"
        ].model_dump()
    )


def run_low_confidence():

    print("\n")
    print("=" * 100)
    print("LOW CONFIDENCE")
    print("=" * 100)

    state = {

        "response_strategy":
            ResponseStrategy.LOW_CONFIDENCE,
    }

    route = strategy_router(
        state
    )

    print(
        f"Route: {route}"
    )

    result = low_confidence_node(
        state
    )

    pprint(
        result[
            "final_answer"
        ].model_dump()
    )


def run_consolidate():

    print("\n")
    print("=" * 100)
    print("CONSOLIDATE")
    print("=" * 100)

    state = {

        "response_strategy":
            ResponseStrategy.CONSOLIDATE,
    }

    route = strategy_router(
        state
    )

    print(
        f"Route: {route}"
    )


def run_conflict_resolution():

    print("\n")
    print("=" * 100)
    print("CONFLICT RESOLUTION")
    print("=" * 100)

    state = {

        "response_strategy":
            ResponseStrategy.RESOLVE_CONFLICT,
    }

    route = strategy_router(
        state
    )

    print(
        f"Route: {route}"
    )


run_direct_response()

run_consolidate()

run_conflict_resolution()

run_low_confidence()