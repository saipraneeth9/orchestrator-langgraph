from enum import Enum

from pydantic import BaseModel, Field


class IntentType(str, Enum):

    POLICY_LOOKUP = "policy_lookup"

    INCIDENT_LOOKUP = "incident_lookup"

    TROUBLESHOOTING = "troubleshooting"

    HOW_TO = "how_to"

    ROOT_CAUSE_ANALYSIS = "root_cause_analysis"

    GENERAL_KNOWLEDGE = "general_knowledge"


class IntentResult(BaseModel):

    primary_intent: IntentType

    confidence: float = Field(
        ge=0,
        le=1
    )

    reasoning: str