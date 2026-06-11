import json
import os

from schemas.source_performance import (
    SourcePerformance,
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.tracing import (
    Timer,
)


METRICS_FILE = "data/source_metrics.json"


def source_performance_node(state):

    responses = state.get(
        "classified_responses",
        [],
    )

    with Timer() as timer:

        metrics = {}

        if os.path.exists(
            METRICS_FILE,
        ):

            try:

                with open(
                    METRICS_FILE,
                    "r",
                ) as file:

                    metrics = json.load(
                        file
                    )

            except (
                json.JSONDecodeError,
                OSError,
            ):

                metrics = {}

        performance = []

        for response in responses:

            source_metrics = metrics.get(
                response.source,
                {},
            )

            queries_seen = max(
                source_metrics.get(
                    "queries_seen",
                    0,
                ),
                1,
            )

            selected = source_metrics.get(
                "selected_as_primary",
                0,
            )

            conflict_wins = source_metrics.get(
                "conflict_wins",
                0,
            )

            success_rate = round(
                selected / queries_seen,
                2,
            )

            conflict_win_rate = round(
                conflict_wins / queries_seen,
                2,
            )

            performance_score = round(
                (success_rate * 0.70)
                + (conflict_win_rate * 0.30),
                2,
            )

            performance.append(
                SourcePerformance(
                    source=response.source,
                    queries_seen=queries_seen,
                    selected_as_primary=selected,
                    conflict_wins=conflict_wins,
                    average_confidence=success_rate,
                    performance_score=performance_score,
                )
            )

    return {
        "source_performance": performance,
        "execution_trace": [
            TraceEvent(
                node="source_performance",
                status="success",
                duration_ms=round(
                    timer.duration_ms,
                    2,
                ),
                metadata={
                    "sources": len(
                        performance
                    ),
                },
            )
        ],
    }