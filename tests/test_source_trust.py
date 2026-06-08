from pprint import pprint

from orchestrator.source_trust import (
    source_trust_node,
)

from schemas.normalized_agent_response import (
    NormalizedAgentResponse,
)

from schemas.answer_type import (
    AnswerType,
)


state = {

    "classified_responses": [

        NormalizedAgentResponse(

            source="servicenow",

            answer=(
                "PTO approvals are failing "
                "due to integration latency."
            ),

            answer_type=
                AnswerType.ROOT_CAUSE,
        ),

        NormalizedAgentResponse(

            source="confluence",

            answer=(
                "Approvals are processed "
                "through Workday."
            ),

            answer_type=
                AnswerType.PROCESS,
        ),

        NormalizedAgentResponse(

            source="sharepoint",

            answer=(
                "Employees receive "
                "20 PTO days annually."
            ),

            answer_type=
                AnswerType.POLICY,
        ),

        NormalizedAgentResponse(

            source="barnum",

            answer=(
                "Several users reported "
                "intermittent approval delays."
            ),

            answer_type=
                AnswerType.OBSERVATION,
        ),
    ]
}

result = source_trust_node(
    state
)

print("\n")
print("=" * 100)
print("SOURCE TRUST")
print("=" * 100)

for trust in result[
    "source_trust"
]:

    pprint(
        trust.model_dump()
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