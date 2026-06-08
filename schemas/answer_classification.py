from pydantic import BaseModel

from schemas.answer_type import (
    AnswerType,
)


class AnswerClassification(
    BaseModel
):

    answer_type: AnswerType

    reasoning: str