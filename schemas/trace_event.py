from pydantic import BaseModel

from typing import Any


class TraceEvent(BaseModel):

    node: str

    status: str

    duration_ms: float

    metadata: dict[str, Any]