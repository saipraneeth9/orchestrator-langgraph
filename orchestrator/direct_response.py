from schemas.final_answer import (
    FinalAnswer,
    SourceReference,
)

from schemas.trace_event import (
    TraceEvent,
)


def direct_response_node(
    state,
):

    aggregated_answers = state.get(
        "aggregated_answers"
    )

    primary_answer = (
        aggregated_answers
        .primary_answer
    )

    reference = SourceReference(

        source=
            primary_answer.source,

        title=
            "Primary Agent Answer",

        evidence_type=
            "agent_answer",
    )

    return {

        "final_answer":

            FinalAnswer(

                answer=
                    primary_answer.answer,

                confidence=
                    1.0,

                references=[
                    reference
                ],

                primary_reference=
                    reference,
            ),

        "execution_trace": [

            TraceEvent(

                node=
                    "direct_response",

                status=
                    "success",

                duration_ms=0,

                metadata={
                    "source":
                        primary_answer.source,
                }
            )
        ]
    }