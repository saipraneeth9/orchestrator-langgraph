from config.source_registry import (
    SOURCE_REGISTRY,
)

from schemas.source_trust import (
    SourceTrust,
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.tracing import (
    Timer,
)


def determine_trust_tier(
    score: float,
) -> str:

    if score >= 0.85:
        return "HIGH"

    if score >= 0.70:
        return "MEDIUM"

    return "LOW"


def source_trust_node(state):

    responses = state.get("classified_responses", [])

    retrieval_results = state.get("retrieval_results", [])

    with Timer() as timer:
        source_trust = []

        total_results = max(
            len(retrieval_results),
            1,
        )

        for response in responses:
            config = SOURCE_REGISTRY.get(
                response.source,
                {},
            )

            authority = config.get(
                "authority",
                0.5,
            )

            evidence_type = config.get(
                "evidence_type",
                "unknown",
            )

            source_results = [
                result
                for result in retrieval_results
                if result.source == response.source
            ]

            evidence_strength = min(
                len(source_results) / 5,
                1.0,
            )

            coverage_score = round(
                len(source_results) / total_results,
                2,
            )

            source_type_confidence = {
                "incident": 1.00,
                "knowledge_article": 0.95,
                "policy": 0.90,
                "community_knowledge": 0.70,
            }.get(
                evidence_type,
                0.50,
            )

            trust_score = round(
                (authority * 0.75)
                + (evidence_strength * 0.10)
                + (source_type_confidence * 0.10)
                + (coverage_score * 0.05),
                2,
            )

            source_trust.append(
                SourceTrust(
                    source=response.source,
                    base_authority=authority,
                    evidence_strength=evidence_strength,
                    source_type_confidence=source_type_confidence,
                    coverage_score=coverage_score,
                    trust_score=trust_score,
                )
            )

        source_trust.sort(
            key=lambda x: x.trust_score,
            reverse=True,
        )

        for index, trust in enumerate(
            source_trust,
            start=1,
        ):
            trust.trust_rank = index

            trust.trust_tier = determine_trust_tier(trust.trust_score)

    return {
        "source_trust": source_trust,
        "execution_trace": [
            TraceEvent(
                node="source_trust",
                status="success",
                duration_ms=round(
                    timer.duration_ms,
                    2,
                ),
                metadata={
                    "sources": len(source_trust),
                },
            )
        ],
    }
