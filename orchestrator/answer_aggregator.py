from schemas.aggregated_answers import (
    AggregatedAnswers,
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.conflict_detector import (
    analyze_conflicts,
)

from utils.tracing import (
    Timer,
)


def answer_aggregator_node(state):

    responses = state.get("classified_responses", [])

    source_trust = {
        trust.source: trust.trust_score for trust in state.get("source_trust", [])
    }

    if not responses:
        return {
            "aggregated_answers": None,
            "execution_trace": [
                TraceEvent(
                    node="answer_aggregator",
                    status="skipped",
                    duration_ms=0,
                    metadata={
                        "reason": "No classified responses",
                    },
                )
            ],
        }

    with Timer() as timer:
        ranked_responses = sorted(
            responses,
            key=lambda response: source_trust.get(response.source, 0.5),
            reverse=True,
        )

        primary_answer = ranked_responses[0]

        supporting_answers = ranked_responses[1:]

        conflict_analysis = analyze_conflicts(ranked_responses)

        aggregated_answers = AggregatedAnswers(
            primary_answer=primary_answer,
            supporting_answers=supporting_answers,
            conflict_analysis=conflict_analysis,
        )

    return {
        "aggregated_answers": aggregated_answers,
        "execution_trace": [
            TraceEvent(
                node="answer_aggregator",
                status="success",
                duration_ms=round(timer.duration_ms, 2),
                metadata={
                    "responses": len(ranked_responses),
                    "primary_source": primary_answer.source,
                    "primary_source_trust": source_trust.get(
                        primary_answer.source, 0.5
                    ),
                    "trust_gap": round(
                        source_trust.get(primary_answer.source, 0.5)
                        - source_trust.get(supporting_answers[0].source, 0.5),
                        2,
                    )
                    if supporting_answers
                    else 1.0,
                    "conflict_detected": (conflict_analysis.conflict_detected),
                    "consensus_score": (conflict_analysis.consensus_score),
                    "confidence_score": (conflict_analysis.confidence_score),
                    "minimum_similarity": (conflict_analysis.minimum_similarity),
                    "average_similarity": (conflict_analysis.average_similarity),
                },
            )
        ],
    }
