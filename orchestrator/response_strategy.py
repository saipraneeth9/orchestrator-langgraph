from schemas.response_strategy import (
    ResponseStrategy,
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.tracing import (
    Timer,
)


LOW_CONFIDENCE_THRESHOLD = 0.50


def response_strategy_node(state):

    aggregated_answers = state.get("aggregated_answers")

    validation_result = state.get("validation_result")

    with Timer() as timer:
        # primary_answer = aggregated_answers.primary_answer

        supporting_answers = aggregated_answers.supporting_answers

        conflict_analysis = aggregated_answers.conflict_analysis

        topology = state.get("answer_topology")

    if topology.conflicting_answers:
        strategy = ResponseStrategy.RESOLVE_CONFLICT

    elif validation_result.confidence_score < LOW_CONFIDENCE_THRESHOLD:
        strategy = ResponseStrategy.LOW_CONFIDENCE

    elif topology.redundant_answers:
        strategy = ResponseStrategy.DIRECT_RESPONSE

    elif topology.complementary_answers:
        strategy = ResponseStrategy.CONSOLIDATE

    else:
        strategy = ResponseStrategy.DIRECT_RESPONSE

    return {
        "response_strategy": strategy,
        "execution_trace": [
            TraceEvent(
                node="response_strategy",
                status="success",
                duration_ms=round(timer.duration_ms, 2),
                metadata={
                    "strategy": strategy.value,
                    "confidence_score": validation_result.confidence_score,
                    "conflict_detected": conflict_analysis.conflict_detected,
                    "supporting_answers": len(supporting_answers),
                },
            )
        ],
    }
