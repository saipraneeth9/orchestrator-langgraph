from pprint import pprint

from agents.servicenow_agent import (
    servicenow_agent,
)

from orchestrator.response_normalizer import (
    response_normalizer_node,
)

from orchestrator.answer_classifier import (
    answer_classifier_node,
)

from orchestrator.answer_aggregator import (
    answer_aggregator_node,
)

from orchestrator.answer_synthesizer import (
    answer_synthesizer_node,
)

state = {

    "query":
        "Why are PTO approvals failing?"
}

state.update(
    servicenow_agent(state)
)

state.update(
    response_normalizer_node(state)
)

state.update(
    answer_classifier_node(state)
)

state.update(
    answer_aggregator_node(state)
)

state.update(
    answer_synthesizer_node(state)
)

print("\n")
print("=" * 100)
print("FINAL ANSWER")
print("=" * 100)

pprint(
    state[
        "final_answer"
    ].model_dump()
)