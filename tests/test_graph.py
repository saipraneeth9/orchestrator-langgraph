from pprint import pprint

from orchestrator.graph import graph


state = graph.invoke(
    {
        "query":
            "Why are PTO approvals failing?"
    }
)

print("\n")
print("=" * 100)
print("FINAL ANSWER")
print("=" * 100)

pprint(
    state["final_answer"].model_dump()
)

print("\n")
print("=" * 100)
print("EXECUTION TRACE")
print("=" * 100)

for event in state["execution_trace"]:

    if hasattr(event, "model_dump"):

        pprint(
            event.model_dump()
        )

    else:

        pprint(
            event
        )