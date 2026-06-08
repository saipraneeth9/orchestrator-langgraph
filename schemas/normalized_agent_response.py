from pydantic import BaseModel

from schemas.answer_type import (
    AnswerType,
)


class NormalizedAgentResponse(BaseModel):

    source: str

    answer: str

    answer_type: (
        AnswerType
        | None
    ) = None

    confidence: float | None = None

    raw_response: dict | None = None