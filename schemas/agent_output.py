from pydantic import BaseModel


class AgentOutput(BaseModel):

    source: str

    response: dict