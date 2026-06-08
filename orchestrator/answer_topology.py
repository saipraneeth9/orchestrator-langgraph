from schemas.answer_topology import (
    AnswerTopology,
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.tracing import (
    Timer,
)


def answer_topology_node(state):

    classified_responses = state.get(
        "classified_responses",
        []
    )

    aggregated_answers = state.get(
        "aggregated_answers"
    )

    with Timer() as timer:

        answer_types = {

            response.answer_type

            for response

            in classified_responses

            if response.answer_type
        }

        source_count = len(
            classified_responses
        )

        unique_answer_types = len(
            answer_types
        )

        conflict_analysis = (
            aggregated_answers
            .conflict_analysis
        )

        conflicting_answers = (
            conflict_analysis
            .conflict_detected
        )

        complementary_answers = (

            unique_answer_types

            >

            1

            and

            not conflicting_answers
        )

        redundant_answers = (

            unique_answer_types

            ==

            1

            and

            not conflicting_answers
        )

        topology = (

            AnswerTopology(

                source_count=
                    source_count,

                unique_answer_types=
                    unique_answer_types,

                complementary_answers=
                    complementary_answers,

                redundant_answers=
                    redundant_answers,

                conflicting_answers=
                    conflicting_answers,

                consensus_strength=
                    conflict_analysis
                    .consensus_score,
            )
        )

    return {

        "answer_topology":
            topology,

        "execution_trace": [

            TraceEvent(

                node=
                    "answer_topology",

                status=
                    "success",

                duration_ms=
                    round(
                        timer.duration_ms,
                        2
                    ),

                metadata={

                    "source_count":
                        source_count,

                    "unique_answer_types":
                        unique_answer_types,

                    "complementary_answers":
                        complementary_answers,

                    "redundant_answers":
                        redundant_answers,

                    "conflicting_answers":
                        conflicting_answers,
                }
            )
        ]
    }