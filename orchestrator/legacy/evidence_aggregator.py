from config.source_registry import (
    SOURCE_REGISTRY,
)

from schemas.evidence_package import (
    EvidencePackage,
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.tracing import (
    Timer,
)


def evidence_aggregator_node(state):

    top_results = state.get(
        "top_results",
        []
    )

    with Timer() as timer:

        evidence_packages = []

        seen_documents = set()

        for result in top_results:

            dedupe_key = (

                result.title.lower().strip(),

                result.content.lower().strip(),
            )

            if dedupe_key in seen_documents:

                continue

            seen_documents.add(
                dedupe_key
            )

            source_metadata = (
                SOURCE_REGISTRY.get(
                    result.source,
                    {}
                )
            )

            authority_score = (
                source_metadata.get(
                    "authority",
                    0.5
                )
            )

            evidence_type = (
                source_metadata.get(
                    "evidence_type",
                    "unknown"
                )
            )

            evidence_packages.append(

                EvidencePackage(

                    source=result.source,

                    evidence_type=
                        evidence_type,

                    title=result.title,

                    content=result.content,

                    authority_score=
                        authority_score,

                    relevance_score=
                        result.relevance_score,

                    final_score=
                        result.final_score,
                )
            )

    return {

        "evidence_packages":
            evidence_packages,

        "execution_trace": [
            TraceEvent(
                node="evidence_aggregator",
                status="success",
                duration_ms=round(
                    timer.duration_ms,
                    2
                ),
                metadata={
                    "input_documents":
                        len(
                            top_results
                        ),
                    "evidence_packages":
                        len(
                            evidence_packages
                        ),
                }
            )
        ]
    }