from pydantic import BaseModel


class SourcePerformance(
    BaseModel
):

    source: str

    queries_seen: int = 0

    selected_as_primary: int = 0

    conflict_wins: int = 0

    average_confidence: float = 0.0

    performance_score: float = 0.50