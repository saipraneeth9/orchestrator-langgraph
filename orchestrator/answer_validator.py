from schemas.validation_result import (
    ValidationResult,
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.tracing import (
    Timer,
)


LOW_CONFIDENCE_THRESHOLD = 0.50


def answer_validator_node(state):

    aggregated_answers = state.get(
        "aggregated_answers"
    )

    with Timer() as timer:

        conflict_analysis = (
            aggregated_answers
            .conflict_analysis
        )

        confidence_score = (
            conflict_analysis
            .confidence_score
        )

        if (
            conflict_analysis
            .conflict_detected
        ):

            validation = ValidationResult(

                valid=False,

                status="CONFLICT",

                confidence_score=
                    confidence_score,

                reason=
                    "Conflicting answers detected.",
            )

        elif (
            confidence_score
            <
            LOW_CONFIDENCE_THRESHOLD
        ):

            validation = ValidationResult(

                valid=False,

                status="LOW_CONFIDENCE",

                confidence_score=
                    confidence_score,

                reason=
                    "Confidence below threshold.",
            )

        else:

            validation = ValidationResult(

                valid=True,

                status="VALID",

                confidence_score=
                    confidence_score,
            )

    return {

        "validation_result":
            validation,

        "execution_trace": [

            TraceEvent(

                node=
                    "answer_validator",

                status=
                    "success",

                duration_ms=
                    round(
                        timer.duration_ms,
                        2
                    ),

                metadata={

                    "valid":
                        validation.valid,

                    "status":
                        validation.status,

                    "confidence_score":
                        validation.confidence_score,
                }
            )
        ]
    }