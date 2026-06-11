from schemas.final_answer import (
    FinalAnswer,
)

from schemas.trace_event import (
    TraceEvent,
)


def low_confidence_node(state):

    return {
        "final_answer": FinalAnswer(
            answer=("Available evidence is insufficient to provide a reliable answer."),
            confidence=0.0,
            source_confidence=0.0,
            references=[],
            primary_reference=None,
        ),
        "execution_trace": [
            TraceEvent(
                node="low_confidence", status="success", duration_ms=0, metadata={}
            )
        ],
    }
