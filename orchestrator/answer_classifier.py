from clients.ollama_client import (
    LLMFactory,
)

from schemas.answer_classification import (
    AnswerClassification,
)

from schemas.trace_event import (
    TraceEvent,
)

from prompts.answer_classifier_prompt import (
    ANSWER_CLASSIFIER_PROMPT,
)

from utils.answer_type_rules import (
    classify_by_rules,
)

from utils.tracing import (
    Timer,
)


def answer_classifier_node(
    state,
):

    responses = state.get(
        "normalized_responses",
        []
    )

    if not responses:

        return {

            "classified_responses":
                [],

            "execution_trace": [

                TraceEvent(

                    node=
                        "answer_classifier",

                    status=
                        "skipped",

                    duration_ms=0,

                    metadata={
                        "reason":
                            "No normalized responses",
                    }
                )
            ]
        }

    llm = (
        LLMFactory
        .get_router_llm()
    )

    structured_llm = (
        llm.with_structured_output(
            AnswerClassification
        )
    )

    with Timer() as timer:

        classified_responses = []

        rule_classifications = 0

        llm_classifications = 0

        for response in responses:

            rule_result = (

                classify_by_rules(
                    response.answer
                )
            )

            if rule_result:

                response.answer_type = (
                    rule_result
                )

                classified_responses.append(
                    response
                )

                rule_classifications += 1

                continue

            classification = (

                structured_llm.invoke(

                    [
                        (
                            "system",
                            ANSWER_CLASSIFIER_PROMPT,
                        ),
                        (
                            "human",
                            response.answer,
                        ),
                    ]
                )
            )

            response.answer_type = (
                classification.answer_type
            )

            classified_responses.append(
                response
            )

            llm_classifications += 1

        total = len(
            classified_responses
        )

        rule_hit_rate = round(

            rule_classifications
            / total,

            2,
        )

        llm_fallback_rate = round(

            llm_classifications
            / total,

            2,
        )

    return {

        "classified_responses":
            classified_responses,

        "execution_trace": [

            TraceEvent(

                node=
                    "answer_classifier",

                status=
                    "success",

                duration_ms=
                    round(
                        timer.duration_ms,
                        2
                    ),

                metadata={

                    "responses":
                        total,

                    "rule_classifications":
                        rule_classifications,

                    "llm_classifications":
                        llm_classifications,

                    "rule_hit_rate":
                        rule_hit_rate,

                    "llm_fallback_rate":
                        llm_fallback_rate,
                }
            )
        ]
    }