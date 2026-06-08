from pydantic import BaseModel


class EvidencePackage(BaseModel):

    source: str

    evidence_type: str

    title: str

    content: str

    authority_score: float

    relevance_score: float

    final_score: float