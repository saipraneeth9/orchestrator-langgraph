from clients.ollama_client import LLMFactory

from schemas.intent_result import IntentResult

from prompts.intent_classifier_prompt import (
    INTENT_CLASSIFIER_PROMPT
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.tracing import (
    Timer,
)


def intent_classifier_node(state):

    llm = LLMFactory.get_router_llm()

    structured_llm = llm.with_structured_output(
        IntentResult
    )

    with Timer() as timer:
        response = structured_llm.invoke(
            [
                (
                    "system",
                    INTENT_CLASSIFIER_PROMPT
                ),
                (
                    "human",
                    state["query"]
                )
            ]
        )

    return {

    "intent_result": {

        "primary_intent":
            response.primary_intent.value,

        "confidence":
            response.confidence,

        "reasoning":
            response.reasoning,
    },

    "execution_trace": [

        TraceEvent(

            node=
                "intent_classifier",

            status=
                "success",

            duration_ms=
                round(
                    timer.duration_ms,
                    2
                ),

            metadata={

                "intent":
                    response.primary_intent.value,

                "confidence":
                    response.confidence,
            }
        )
    ]
}