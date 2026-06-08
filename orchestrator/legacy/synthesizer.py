from clients.ollama_client import (
    LLMFactory,
)

from schemas.trace_event import (
    TraceEvent,
)

from prompts.synthesizer_prompt import (
    SYNTHESIZER_PROMPT,
)

from schemas.final_answer import (
    FinalAnswer,
    SourceReference,
)

from utils.tracing import (
    Timer,
)


def synthesizer_node(state):

    query = state["query"]

    evidence_packages = state.get(
        "evidence_packages",
        []
    )

    if not evidence_packages:

        return {

            "final_answer":
                FinalAnswer(
                    answer="No relevant evidence was found.",
                    confidence=0.0,
                    references=[],
                ),

            "execution_trace": [
                TraceEvent(
                    node="synthesizer",
                    status="no_evidence",
                    duration_ms=0,
                    metadata={
                        "confidence": 0.0,
                        "references": 0,
                        "primary_source": None,
                    }
                )
            ]
        }

    with Timer() as timer:

        evidence_blocks = []

        for index, evidence in enumerate(
            evidence_packages,
            start=1,
        ):

            evidence_blocks.append(
                f"""
Evidence #{index}

Source:
{evidence.source}

Title:
{evidence.title}

Type:
{evidence.evidence_type}

Score:
{evidence.final_score:.2f}

Content:
{evidence.content}
"""
            )

        prompt = (
            SYNTHESIZER_PROMPT.format(
                query=query,
                evidence="\n\n".join(
                    evidence_blocks
                ),
            )
        )

        llm = (
            LLMFactory
            .get_synthesizer_llm()
        )

        response = llm.invoke(
            prompt
        )

        confidence = round(

            sum(
                evidence.final_score
                for evidence
                in evidence_packages
            )

            /

            len(
                evidence_packages
            ),

            2,
        )

        references = []

        for evidence in evidence_packages:

            references.append(

                SourceReference(

                    source=
                        evidence.source,

                    title=
                        evidence.title,

                    evidence_type=
                        evidence.evidence_type,
                )
            )

        primary_reference = references[0] if references else None

        final_answer = FinalAnswer(

            answer=
                response.content,

            confidence=
                confidence,

            references=
                references,
            primary_reference=primary_reference,
        )

    return {

        "final_answer":
            final_answer,

        "execution_trace": [
            TraceEvent(
                node="synthesizer",
                status="success",
                duration_ms=round(
                    timer.duration_ms,
                    2
                ),
                metadata={
                    "confidence":
                        confidence,
                    "references":
                        len(
                            references
                        ),
                    "primary_source":
                        primary_reference.source if primary_reference else None,
                }
            )
        ]
    }