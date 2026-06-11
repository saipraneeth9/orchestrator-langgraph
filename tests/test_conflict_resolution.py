from pprint import pprint

from orchestrator.conflict_resolution import (
    conflict_resolution_node,
)

from schemas.aggregated_answers import (
    AggregatedAnswers,
)

from schemas.conflict_analysis import (
    ConflictAnalysis,
)

from schemas.normalized_agent_response import (
    NormalizedAgentResponse,
)

from schemas.source_trust import (
    SourceTrust,
)

state = {
    "aggregated_answers": AggregatedAnswers(
        primary_answer=NormalizedAgentResponse(
            source="servicenow",
            answer=("PTO approvals are failing due to integration latency."),
        ),
        supporting_answers=[
            NormalizedAgentResponse(
                source="confluence",
                answer=("PTO approvals are failing due to permission issues."),
            ),
            NormalizedAgentResponse(
                source="barnum",
                answer=("PTO approvals are failing due to token expiry."),
            ),
        ],
        conflict_analysis=ConflictAnalysis(
            conflict_detected=True,
            consensus_score=0.45,
            minimum_similarity=0.40,
            average_similarity=0.45,
            confidence_score=0.42,
        ),
    ),
    "source_trust": [
        SourceTrust(
            source="servicenow",
            base_authority=1.0,
            evidence_strength=0.0,
            source_type_confidence=1.0,
            coverage_score=0.0,
            trust_score=0.85,
            performance_score=0.87,
            effective_trust=0.86,
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
            performance_score=0.73,
            effective_trust=0.79,
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
            performance_score=0.27,
            effective_trust=0.49,
            trust_rank=3,
            trust_tier="LOW",
        ),
    ],
}

result = conflict_resolution_node(state)

print("\n")
print("=" * 100)
print("FINAL ANSWER")
print("=" * 100)

pprint(result["final_answer"].model_dump())

print("\n")
print("=" * 100)
print("EXECUTION TRACE")
print("=" * 100)

for event in result["execution_trace"]:
    pprint(event.model_dump())
