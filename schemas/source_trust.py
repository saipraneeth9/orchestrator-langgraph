from pydantic import BaseModel


class SourceTrust(
    BaseModel
):

    source: str

    base_authority: float

    evidence_strength: float

    source_type_confidence: float

    coverage_score: float

    trust_score: float

    performance_score: float = 0.0

    effective_trust: float = 0.0

    trust_rank: int | None = None

    trust_tier: str | None = None