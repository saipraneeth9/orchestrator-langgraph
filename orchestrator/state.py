from typing import TypedDict, Annotated
from operator import add

from schemas.final_answer import (
    FinalAnswer,
)

from schemas.trace_event import (
    TraceEvent,
)

from schemas.agent_output import (
    AgentOutput,
)

from schemas.answer_topology import (
    AnswerTopology,
)

from schemas.aggregated_answers import (
    AggregatedAnswers,
)

from schemas.validation_result import (
    ValidationResult,
)

from schemas.response_strategy import (
    ResponseStrategy,
)

from schemas.source_trust import (
    SourceTrust,
)

from schemas.source_performance import (
    SourcePerformance,
)


class OrchestratorState(TypedDict):
    query: str

    intent_result: dict

    retrieval_strategy: dict

    source_selection_result: dict

    agent_outputs: Annotated[
        list[AgentOutput],
        add,
    ]

    normalized_responses: list

    classified_responses: list

    final_answer: FinalAnswer

    execution_trace: Annotated[
        list[TraceEvent],
        add,
    ]

    errors: Annotated[
        list,
        add,
    ]

    answer_topology: AnswerTopology

    source_trust: list

    aggregated_answers: AggregatedAnswers

    validation_result: ValidationResult

    response_strategy: ResponseStrategy

    source_trust: list[SourceTrust]

    source_performance: list[SourcePerformance]
