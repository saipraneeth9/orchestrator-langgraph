from pprint import pprint

from orchestrator.source_performance import (
    source_performance_node,
)

from schemas.normalized_agent_response import (
    NormalizedAgentResponse,
)

state = {

    "classified_responses": [

        NormalizedAgentResponse(
            source="servicenow",
            answer="test",
        ),

        NormalizedAgentResponse(
            source="confluence",
            answer="test",
        ),

        NormalizedAgentResponse(
            source="barnum",
            answer="test",
        ),
    ]
}

result = source_performance_node(
    state
)

print("\n")
print("=" * 100)
print("SOURCE PERFORMANCE")
print("=" * 100)

for item in result[
    "source_performance"
]:
    pprint(
        item.model_dump()
    )