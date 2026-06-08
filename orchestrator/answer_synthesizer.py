from clients.ollama_client import (
    LLMFactory,
)

from schemas.final_answer import (
    FinalAnswer,
    SourceReference,
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.tracing import (
    Timer,
)


def answer_synthesizer_node(state):

    aggregated_answers = state.get(
        "aggregated_answers"
    )

    if not aggregated_answers:

        return {

            "final_answer":
                FinalAnswer(
                    answer=
                        "No agent responses were available.",
                    confidence=0.0,
                    references=[],
                    primary_reference=None,
                ),

            "execution_trace": [

                TraceEvent(

                    node=
                        "answer_synthesizer",

                    status=
                        "no_answers",

                    duration_ms=0,

                    metadata={}
                )
            ]
        }

    primary_answer = (
        aggregated_answers
        .primary_answer
    )

    supporting_answers = (
        aggregated_answers
        .supporting_answers
    )

    conflict_analysis = (
        aggregated_answers
        .conflict_analysis
    )

    with Timer() as timer:

        answer_blocks = [

            f"""
Source:
{primary_answer.source}

Answer:
{primary_answer.answer}
"""
        ]

        for answer in supporting_answers:

            answer_blocks.append(

                f"""
Source:
{answer.source}

Answer:
{answer.answer}
"""
            )

        prompt = f"""
User Query:

{state["query"]}

Agent Answers:

{''.join(answer_blocks)}

Create a single consolidated answer.

Prefer higher authority sources when conflicts exist.

If answers disagree,
favor the most authoritative source.
"""

        llm = (
            LLMFactory
            .get_synthesizer_llm()
        )

        response = llm.invoke(
            prompt
        )

        references = [

            SourceReference(

                source=
                    primary_answer.source,

                title=
                    "Primary Agent Answer",

                evidence_type=
                    "agent_answer",
            )
        ]

        final_answer = (

            FinalAnswer(

                answer=
                    response.content,

                confidence=
                    conflict_analysis
                    .confidence_score,

                references=
                    references,

                primary_reference=
                    references[0],
            )
        )

    return {

        "final_answer":
            final_answer,

        "execution_trace": [

            TraceEvent(

                node=
                    "answer_synthesizer",

                status=
                    "success",

                duration_ms=
                    round(
                        timer.duration_ms,
                        2
                    ),

                metadata={

                    "primary_source":
                        primary_answer.source,

                    "supporting_answers":
                        len(
                            supporting_answers
                        ),

                    "confidence_score":
                        (
                            conflict_analysis
                            .confidence_score
                        ),

                    "conflict_detected":
                        (
                            conflict_analysis
                            .conflict_detected
                        ),
                }
            )
        ]
    }