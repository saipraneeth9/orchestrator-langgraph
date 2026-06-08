from clients.embedding_client import (
    EmbeddingClient,
)

from helpers.similarity_helper import (
    cosine_similarity,
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.tracing import (
    Timer,
)

from copy import deepcopy


def relevance_scorer_node(state):

    query = state["query"]

    retrieval_results = state.get(
        "retrieval_results",
        []
    )

    if not retrieval_results:

        return {

            "scored_results": [],

            "execution_trace": [
                TraceEvent(
                    node="relevance_scorer",
                    status="skipped",
                    duration_ms=0,
                    metadata={
                        "reason":
                            "No retrieval results",
                        "documents_scored": 0,
                    }
                )
            ]
        }

    with Timer() as timer:

        query_embedding = (
            EmbeddingClient.embed_query(
                query
            )
        )

        scored_results = []

        for result in retrieval_results:

            document_text = (
                result.title
                + "\n"
                + result.content
            )

            document_embedding = (
                EmbeddingClient.embed_query(
                    document_text
                )
            )

            scored_result = deepcopy(
                result
            )

            scored_result.relevance_score = (
                cosine_similarity(
                    query_embedding,
                    document_embedding,
                )
            )

            scored_results.append(
                scored_result
            )

    return {

        "scored_results":
            scored_results,

        "execution_trace": [
            TraceEvent(
                node="relevance_scorer",
                status="success",
                duration_ms=round(
                    timer.duration_ms,
                    2
                ),
                metadata={
                    "documents_scored":
                        len(
                            scored_results
                        ),
                }
            )
        ]
    }