from pydantic import BaseModel


class ConflictAnalysis(BaseModel):

    conflict_detected: bool

    consensus_score: float

    confidence_score: float

    minimum_similarity: float

    average_similarity: float