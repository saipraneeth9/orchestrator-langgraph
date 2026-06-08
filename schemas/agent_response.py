from pydantic import BaseModel


class AgentResponse(BaseModel):

    source: str

    answer: str

    confidence: float

    authority_score: float

    citations: list[str] = []