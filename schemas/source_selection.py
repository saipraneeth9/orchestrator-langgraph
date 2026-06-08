from pydantic import BaseModel, Field


class SelectedSource(BaseModel):

    source: str

    authority_score: float = Field(
        ge=0,
        le=1
    )

    reasoning: str


class SourceSelectionResult(BaseModel):

    sources: list[SelectedSource]

    reasoning: str