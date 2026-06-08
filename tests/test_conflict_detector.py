from pprint import pprint

from schemas.normalized_agent_response import (
    NormalizedAgentResponse,
)

from utils.conflict_detector import (
    analyze_conflicts,
)


responses = [

    NormalizedAgentResponse(

        source="servicenow",

        answer=
            "PTO approvals are failing due to integration latency.",
    ),

    NormalizedAgentResponse(

        source="confluence",

        answer=
            "PTO approvals are impacted by latency in workflow integrations.",
    ),

    NormalizedAgentResponse(

        source="barnum",

        answer=
            "Users report approval delays caused by integration latency.",
    ),
]

result = analyze_conflicts(
    responses
)

print("\n")
print("=" * 100)
print("CONFLICT ANALYSIS")
print("=" * 100)

pprint(
    result.model_dump()
)