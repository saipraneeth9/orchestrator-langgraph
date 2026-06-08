from pprint import pprint

from orchestrator.response_normalizer import (
    response_normalizer_node,
)

from schemas.agent_output import (
    AgentOutput,
)

state = {

    "agent_outputs": [

        AgentOutput(

            source="servicenow",

            response={
                "answer":
                    "PTO approvals are failing due to integration latency."
            }
        )
    ]
}

result = response_normalizer_node(
    state
)

print("\n")
print("=" * 100)
print("NORMALIZED RESPONSES")
print("=" * 100)

for response in result[
    "normalized_responses"
]:

    pprint(
        response.model_dump()
    )

print("\n")
print("=" * 100)
print("EXECUTION TRACE")
print("=" * 100)

for event in result[
    "execution_trace"
]:

    pprint(
        event.model_dump()
    )