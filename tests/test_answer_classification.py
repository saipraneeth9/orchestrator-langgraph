from pprint import pprint

from orchestrator.answer_classifier import (
    answer_classifier_node,
)

from schemas.normalized_agent_response import (
    NormalizedAgentResponse,
)


state = {

    "normalized_responses": [

        NormalizedAgentResponse(

            source="servicenow",

            answer=
                "PTO approvals are failing due to integration latency.",
        ),

        NormalizedAgentResponse(

            source="confluence",

            answer=
                "PTO approvals are processed through Workday.",
        ),

        NormalizedAgentResponse(

            source="barnum",

            answer=
                "Users reported intermittent approval delays.",
        ),
    ]
}

result = (
    answer_classifier_node(
        state
    )
)

print("\n")
print("=" * 100)
print("CLASSIFIED RESPONSES")
print("=" * 100)

for response in result[
    "classified_responses"
]:

    pprint(
        response.model_dump()
    )

print("\n")
print("=" * 100)
print("EXECUTION TRACE")
print("=" * 100)

for event in result["execution_trace"]:

    pprint(
        event.model_dump()
    )