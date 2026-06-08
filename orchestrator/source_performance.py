from schemas.source_performance import (
    SourcePerformance,
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.tracing import (
    Timer,
)


def source_performance_node(state):

    responses = state.get("classified_responses", [])

    with Timer() as timer:
        performance = []

        for response in responses:
            performance.append(
                SourcePerformance(
                    source=response.source,
                    queries_seen=100,
                    selected_as_primary=50,
                    conflict_wins=25,
                    average_confidence=0.80,
                    performance_score=0.80,
                )
            )

    return {
        "source_performance": performance,
        "execution_trace": [
            TraceEvent(
                node="source_performance",
                status="success",
                duration_ms=round(timer.duration_ms, 2),
                metadata={"sources": len(performance)},
            )
        ],
    }
