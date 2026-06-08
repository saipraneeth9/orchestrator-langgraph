from pprint import pprint

from orchestrator.answer_aggregator import (
    answer_aggregator_node,
)

from schemas.answer_type import (
    AnswerType,
)

from schemas.normalized_agent_response import (
    NormalizedAgentResponse,
)

from schemas.source_trust import (
    SourceTrust,
)


state = {
    "classified_responses": [
        NormalizedAgentResponse(
            source="servicenow",
            answer=("PTO approvals are failing due to integration latency."),
            answer_type=AnswerType.ROOT_CAUSE,
        ),
        NormalizedAgentResponse(
            source="confluence",
            answer=("PTO approvals are processed through Workday."),
            answer_type=AnswerType.PROCESS,
        ),
        NormalizedAgentResponse(
            source="barnum",
            answer=("Community users reported intermittent approval delays."),
            answer_type=AnswerType.OBSERVATION,
        ),
    ],
    "source_trust": [
        SourceTrust(
            source="servicenow",
            base_authority=1.0,
            evidence_strength=0.0,
            source_type_confidence=1.0,
            coverage_score=0.0,
            trust_score=0.85,
            trust_rank=1,
            trust_tier="HIGH",
        ),
        SourceTrust(
            source="confluence",
            base_authority=0.95,
            evidence_strength=0.0,
            source_type_confidence=0.95,
            coverage_score=0.0,
            trust_score=0.81,
            trust_rank=2,
            trust_tier="MEDIUM",
        ),
        SourceTrust(
            source="barnum",
            base_authority=0.70,
            evidence_strength=0.0,
            source_type_confidence=0.70,
            coverage_score=0.0,
            trust_score=0.59,
            trust_rank=3,
            trust_tier="LOW",
        ),
    ],
}

result = answer_aggregator_node(state)

print("\n")
print("=" * 100)
print("AGGREGATED ANSWERS")
print("=" * 100)

pprint(result["aggregated_answers"].model_dump())

print("\n")
print("=" * 100)
print("EXECUTION TRACE")
print("=" * 100)

for event in result["execution_trace"]:
    pprint(event.model_dump())
