from pydantic import BaseModel

from schemas.normalized_agent_response import (
    NormalizedAgentResponse,
)

from schemas.conflict_analysis import (
    ConflictAnalysis,
)


class AggregatedAnswers(BaseModel):

    primary_answer: (
        NormalizedAgentResponse
    )

    supporting_answers: list[
        NormalizedAgentResponse
    ]

    conflict_analysis: (
        ConflictAnalysis
    )