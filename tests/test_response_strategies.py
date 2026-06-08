from pprint import pprint

from orchestrator.response_strategy import (
    response_strategy_node,
)

from schemas.aggregated_answers import (
    AggregatedAnswers,
)

from schemas.answer_topology import (
    AnswerTopology,
)

from schemas.conflict_analysis import (
    ConflictAnalysis,
)

from schemas.normalized_agent_response import (
    NormalizedAgentResponse,
)

from schemas.validation_result import (
    ValidationResult,
)


def run_test(
    test_name,
    aggregated_answers,
    validation_result,
    answer_topology,
):

    print("\n")
    print("=" * 100)
    print(test_name)
    print("=" * 100)

    state = {

        "aggregated_answers":
            aggregated_answers,

        "validation_result":
            validation_result,

        "answer_topology":
            answer_topology,
    }

    result = response_strategy_node(
        state
    )

    pprint(
        {
            "strategy":
                result[
                    "response_strategy"
                ]
        }
    )

    print("\nTRACE")

    for event in result[
        "execution_trace"
    ]:

        pprint(
            event.model_dump()
        )


# ==================================================
# DIRECT_RESPONSE
# ==================================================

run_test(

    "DIRECT_RESPONSE",

    AggregatedAnswers(

        primary_answer=
            NormalizedAgentResponse(
                source="servicenow",
                answer="Integration latency caused PTO failures.",
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

    ValidationResult(
        valid=True,
        status="VALID",
        confidence_score=1.0,
    ),

    AnswerTopology(
        source_count=1,
        unique_answer_types=1,
        complementary_answers=False,
        redundant_answers=True,
        conflicting_answers=False,
        consensus_strength=1.0,
    ),
)

# ==================================================
# CONSOLIDATE
# ==================================================

run_test(

    "CONSOLIDATE",

    AggregatedAnswers(

        primary_answer=
            NormalizedAgentResponse(
                source="servicenow",
                answer="Integration latency caused PTO failures.",
            ),

        supporting_answers=[

            NormalizedAgentResponse(
                source="confluence",
                answer="Approvals are processed through Workday.",
            ),

            NormalizedAgentResponse(
                source="sharepoint",
                answer="Employees receive 20 PTO days annually.",
            ),
        ],

        conflict_analysis=
            ConflictAnalysis(
                conflict_detected=False,
                consensus_score=1.0,
                minimum_similarity=1.0,
                average_similarity=1.0,
                confidence_score=0.95,
            ),
    ),

    ValidationResult(
        valid=True,
        status="VALID",
        confidence_score=0.95,
    ),

    AnswerTopology(
        source_count=3,
        unique_answer_types=3,
        complementary_answers=True,
        redundant_answers=False,
        conflicting_answers=False,
        consensus_strength=1.0,
    ),
)

# ==================================================
# RESOLVE_CONFLICT
# ==================================================

run_test(

    "RESOLVE_CONFLICT",

    AggregatedAnswers(

        primary_answer=
            NormalizedAgentResponse(
                source="servicenow",
                answer="Root cause is latency.",
            ),

        supporting_answers=[

            NormalizedAgentResponse(
                source="confluence",
                answer="Root cause is permissions.",
            ),

            NormalizedAgentResponse(
                source="barnum",
                answer="Root cause is expired token.",
            ),
        ],

        conflict_analysis=
            ConflictAnalysis(
                conflict_detected=True,
                consensus_score=0.42,
                minimum_similarity=0.32,
                average_similarity=0.42,
                confidence_score=0.42,
            ),
    ),

    ValidationResult(
        valid=False,
        status="CONFLICT",
        confidence_score=0.42,
    ),

    AnswerTopology(
        source_count=3,
        unique_answer_types=1,
        complementary_answers=False,
        redundant_answers=False,
        conflicting_answers=True,
        consensus_strength=0.42,
    ),
)

# ==================================================
# LOW_CONFIDENCE
# ==================================================

run_test(

    "LOW_CONFIDENCE",

    AggregatedAnswers(

        primary_answer=
            NormalizedAgentResponse(
                source="servicenow",
                answer="Unknown cause.",
            ),

        supporting_answers=[],

        conflict_analysis=
            ConflictAnalysis(
                conflict_detected=False,
                consensus_score=0.25,
                minimum_similarity=0.25,
                average_similarity=0.25,
                confidence_score=0.25,
            ),
    ),

    ValidationResult(
        valid=False,
        status="LOW_CONFIDENCE",
        confidence_score=0.25,
    ),

    AnswerTopology(
        source_count=1,
        unique_answer_types=1,
        complementary_answers=False,
        redundant_answers=True,
        conflicting_answers=False,
        consensus_strength=0.25,
    ),
)