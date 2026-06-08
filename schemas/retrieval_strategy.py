from pydantic import BaseModel


class RetrievalStrategy(BaseModel):

    search_incidents: bool = False

    search_documentation: bool = False

    search_community: bool = False

    prefer_recall: bool = False

    prefer_precision: bool = False

    max_sources: int = 3

    reasoning: str