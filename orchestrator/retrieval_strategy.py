from config.retrieval_policy import (
    RETRIEVAL_POLICY,
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.tracing import (
    Timer,
)


def retrieval_strategy_node(state):

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

        strategy = (
            RETRIEVAL_POLICY.get(
                intent,
                RETRIEVAL_POLICY[
                    "general_knowledge"
                ]
            )
        )

    return {

        "retrieval_strategy":
            strategy,

        "execution_trace": [

            TraceEvent(

                node=
                    "retrieval_strategy",

                status=
                    "success",

                duration_ms=
                    round(
                        timer.duration_ms,
                        2
                    ),

                metadata={

                    "search_incidents":
                        strategy[
                            "search_incidents"
                        ],

                    "search_documentation":
                        strategy[
                            "search_documentation"
                        ],

                    "search_community":
                        strategy[
                            "search_community"
                        ],

                    "max_sources":
                        strategy[
                            "max_sources"
                        ],
                }
            )
        ]
    }