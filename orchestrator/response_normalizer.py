from schemas.normalized_agent_response import (
    NormalizedAgentResponse,
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.response_extractor import (
    extract_answer,
)

from utils.tracing import (
    Timer,
)


def response_normalizer_node(state):

    agent_outputs = state.get(
        "agent_outputs",
        []
    )

    with Timer() as timer:

        normalized_responses = []

        for output in agent_outputs:

            normalized_responses.append(

                NormalizedAgentResponse(

                    source=
                        output.source,

                    answer=
                        extract_answer(
                            output.response
                        ),

                    raw_response=
                        output.response,
                )
            )

    return {

        "normalized_responses":
            normalized_responses,

        "execution_trace": [

            TraceEvent(

                node=
                    "response_normalizer",

                status=
                    "success",

                duration_ms=
                    round(
                        timer.duration_ms,
                        2
                    ),

                metadata={
                    "responses":
                        len(
                            normalized_responses
                        )
                }
            )
        ]
    }