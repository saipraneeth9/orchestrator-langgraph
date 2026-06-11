from pydantic import BaseModel


class SourceReference(BaseModel):

    source: str

    title: str

    evidence_type: str


class FinalAnswer(BaseModel):

    answer: str

    confidence: float

    source_confidence: float

    references: list[SourceReference]

    primary_reference: SourceReference | None