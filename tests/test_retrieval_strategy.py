from pprint import pprint

from orchestrator.retrieval_strategy import (
    retrieval_strategy_node
)


state = {
    "intent_result": {
        "primary_intent": "root_cause_analysis"
    }
}

result = retrieval_strategy_node(state)

pprint(result)