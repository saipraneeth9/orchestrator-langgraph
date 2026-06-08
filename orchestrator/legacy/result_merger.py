from schemas.trace_event import (
    TraceEvent,
)

from utils.tracing import (
    Timer,
)


def result_merger_node(state):
    """
    Fan-in aggregation node.

    At this stage we only collect metrics
    and verify that LangGraph merged all
    retrieval results correctly.

    Future responsibilities:

    - Deduplication
    - Ranking
    - Reranking
    - Evidence selection
    - LLM synthesis
    """

    retrieval_results = state.get(
        "retrieval_results",
        []
    )

    with Timer() as timer:

        source_counts = {}

        for result in retrieval_results:

            source = result.source

            source_counts[source] = (
                source_counts.get(source, 0)
                + 1
            )

    return {

        "execution_trace": [
            TraceEvent(
                node="result_merger",
                status="success",
                duration_ms=round(
                    timer.duration_ms,
                    2
                ),
                metadata={
                    "merged_results":
                        len(retrieval_results),
                }
            )
        ]
    }