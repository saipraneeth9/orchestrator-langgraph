from pprint import pprint

from agents.servicenow_agent import (
    servicenow_agent,
)

state = {

    "query":
        "Why are PTO approvals failing?"
}

result = servicenow_agent(
    state
)

print("\n")
print("=" * 100)
print("RAW RESULT")
print("=" * 100)

pprint(result)