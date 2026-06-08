from config.source_registry import (
    SOURCE_REGISTRY,
)

from config.ranking_policy import (
    RANKING_POLICY,
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.tracing import (
    Timer,
)

TOP_K = 5


def ranker_node(state):

    scored_results = state.get(
    "scored_results",
    []
)

    intent = (
        state
        .get(
            "intent_result",
            {}
        )
        .get(
            "primary_intent",
            "general_knowledge"
        )
    )

    with Timer() as timer:

        policy = (
            RANKING_POLICY.get(
                intent,
                RANKING_POLICY[
                    "general_knowledge"
                ]
            )
        )

        relevance_weight = (
            policy[
                "relevance_weight"
            ]
        )

        authority_weight = (
            policy[
                "authority_weight"
            ]
        )

        ranked_results = []

        for result in scored_results:

            authority_score = (
                SOURCE_REGISTRY
                .get(
                    result.source,
                    {}
                )
                .get(
                    "authority",
                    0.5
                )
            )

            result.final_score = (

                relevance_weight
                * result.relevance_score

                +

                authority_weight
                * authority_score
            )

            ranked_results.append(
                result
            )

        ranked_results.sort(
            key=lambda x: x.final_score,
            reverse=True,
        )

        top_results = ranked_results[
            :TOP_K
        ]

    return {

        "ranked_results":
            ranked_results,

        "top_results":
            top_results,

        "execution_trace": [
            TraceEvent(
                node="ranker",
                status="success",
                duration_ms=round(
                    timer.duration_ms,
                    2
                ),
                metadata={
                    "documents_ranked":
                        len(
                            ranked_results
                        ),
                    "top_k":
                        len(
                            top_results
                        ),
                }
            )
        ]
    }