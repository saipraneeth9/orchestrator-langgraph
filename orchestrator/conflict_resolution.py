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


HIGH_CONFIDENCE_GAP = 0.10

LOW_CONFIDENCE_GAP = 0.03


def conflict_resolution_node(state):

    aggregated_answers = state.get(
        "aggregated_answers"
    )

    if not aggregated_answers:

        return {

            "final_answer":

                FinalAnswer(

                    answer=
                        "No evidence available for conflict resolution.",

                    confidence=0.0,

                    references=[],

                    primary_reference=None,
                ),

            "execution_trace": [

                TraceEvent(

                    node=
                        "conflict_resolution",

                    status=
                        "skipped",

                    duration_ms=0,

                    metadata={
                        "reason":
                            "No aggregated answers",
                    },
                )
            ],
        }

    source_trust = state.get(
        "source_trust",
        []
    )

    trust_lookup = {

        trust.source: trust

        for trust

        in source_trust
    }

    with Timer() as timer:

        primary_answer = (
            aggregated_answers
            .primary_answer
        )

        supporting_answers = (
            aggregated_answers
            .supporting_answers
        )

        primary_trust = (
            trust_lookup.get(
                primary_answer.source
            )
        )

        highest_trust_score = (

            primary_trust.trust_score

            if primary_trust

            else 0.0
        )

        # --------------------------------------------------
        # Single Source
        # --------------------------------------------------

        if not supporting_answers:

            reference = SourceReference(

                source=
                    primary_answer.source,

                title=
                    "Single Source Resolution",

                evidence_type=
                    "agent_answer",
            )

            final_answer = FinalAnswer(

                answer=
                    primary_answer.answer,

                confidence=
                    highest_trust_score,

                references=[
                    reference
                ],

                primary_reference=
                    reference,
            )

            metadata = {

                "resolution_method":
                    "single_source",
            }

        else:

            competing_score = 0.0

            for answer in supporting_answers:

                trust = trust_lookup.get(
                    answer.source
                )

                if trust:

                    competing_score = max(

                        competing_score,

                        trust.trust_score,
                    )

            trust_gap = round(

                highest_trust_score

                -

                competing_score,

                2,
            )

            # --------------------------------------------------
            # Deterministic Resolution
            # --------------------------------------------------

            if trust_gap >= HIGH_CONFIDENCE_GAP:

                reference = SourceReference(

                    source=
                        primary_answer.source,

                    title=
                        "Highest Trust Source",

                    evidence_type=
                        "trust_resolution",
                )

                final_answer = FinalAnswer(

                    answer=
                        primary_answer.answer,

                    confidence=
                        highest_trust_score,

                    references=[
                        reference
                    ],

                    primary_reference=
                        reference,
                )

                metadata = {

                    "resolution_method":
                        "trust_based",

                    "winning_source":
                        primary_answer.source,

                    "winning_trust":
                        highest_trust_score,

                    "trust_gap":
                        trust_gap,
                }

            # --------------------------------------------------
            # Trust With Alternatives
            # --------------------------------------------------

            elif trust_gap >= LOW_CONFIDENCE_GAP:

                alternatives = [

                    f"{answer.source}: {answer.answer}"

                    for answer

                    in supporting_answers
                ]

                reference = SourceReference(

                    source=
                        primary_answer.source,

                    title=
                        "Trust Based Resolution",

                    evidence_type=
                        "trust_resolution",
                )

                final_answer = FinalAnswer(

                    answer=(

                        f"{primary_answer.answer}\n\n"

                        f"Alternative viewpoints:\n\n"

                        f"{chr(10).join(alternatives)}"
                    ),

                    confidence=
                        highest_trust_score,

                    references=[
                        reference
                    ],

                    primary_reference=
                        reference,
                )

                metadata = {

                    "resolution_method":
                        "trust_with_alternatives",

                    "winning_source":
                        primary_answer.source,

                    "trust_gap":
                        trust_gap,
                }

            # --------------------------------------------------
            # LLM Resolution
            # --------------------------------------------------

            else:

                evidence = [

                    f"""
Source:
{primary_answer.source}

Trust Score:
{highest_trust_score}

Answer:
{primary_answer.answer}
"""
                ]

                for answer in supporting_answers:

                    trust = trust_lookup.get(
                        answer.source
                    )

                    score = (

                        trust.trust_score

                        if trust

                        else 0.0
                    )

                    evidence.append(

                        f"""
Source:
{answer.source}

Trust Score:
{score}

Answer:
{answer.answer}
"""
                    )

                prompt = f"""
Multiple trusted sources disagree.

Evaluate the evidence.

Rules:

1. Prefer higher trust scores.
2. Consider source authority.
3. Consider answer quality.
4. Explain uncertainty if needed.

Evidence:

{''.join(evidence)}

Provide:

- Most likely answer
- Alternative explanations
- Confidence assessment
"""

                llm = (
                    LLMFactory
                    .get_synthesizer_llm()
                )

                response = llm.invoke(
                    prompt
                )

                reference = SourceReference(

                    source=
                        primary_answer.source,

                    title=
                        "Conflict Resolution",

                    evidence_type=
                        "conflict_analysis",
                )

                final_answer = FinalAnswer(

                    answer=
                        response.content,

                    confidence=
                        round(
                            highest_trust_score,
                            2
                        ),

                    references=[
                        reference
                    ],

                    primary_reference=
                        reference,
                )

                metadata = {

                    "resolution_method":
                        "llm_resolution",

                    "primary_source":
                        primary_answer.source,

                    "primary_trust":
                        highest_trust_score,

                    "trust_gap":
                        trust_gap,

                    "sources_compared":
                        len(
                            supporting_answers
                        ) + 1,
                }

    return {

        "final_answer":
            final_answer,

        "execution_trace": [

            TraceEvent(

                node=
                    "conflict_resolution",

                status=
                    "success",

                duration_ms=
                    round(
                        timer.duration_ms,
                        2
                    ),

                metadata=
                    metadata,
            )
        ],
    }