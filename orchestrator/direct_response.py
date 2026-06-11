from schemas.final_answer import (
    FinalAnswer,
    SourceReference,
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.trust import (
    get_effective_trust,
)


def direct_response_node(state):

    aggregated_answers = state.get(
        "aggregated_answers"
    )

    primary_answer = (
        aggregated_answers
        .primary_answer
    )

    reference = SourceReference(
        source=primary_answer.source,
        title="Primary Agent Answer",
        evidence_type="agent_answer",
    )

    source_confidence = get_effective_trust(
        primary_answer.source,
        state.get("source_trust", []),
    )

    return {
        "final_answer": FinalAnswer(
            answer=primary_answer.answer,
            confidence=1.0,
            source_confidence=source_confidence,
            references=[reference],
            primary_reference=reference,
        ),
        "execution_trace": [
            TraceEvent(
                node="direct_response",
                status="success",
                duration_ms=0,
                metadata={
                    "source": primary_answer.source,
                },
            )
        ],
    }