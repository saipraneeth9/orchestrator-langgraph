from pydantic import BaseModel


class ValidationResult(BaseModel):

    valid: bool

    status: str

    confidence_score: float

    reason: str | None = None