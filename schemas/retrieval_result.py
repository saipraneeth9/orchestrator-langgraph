from pydantic import BaseModel


class RetrievalResult(BaseModel):

    source: str

    title: str

    content: str

    relevance_score: float = 0.0

    final_score: float = 0.0