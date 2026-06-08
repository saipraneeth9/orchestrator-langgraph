from pprint import pprint

from orchestrator.graph import graph

from orchestrator.legacy.relevance_scorer import (
    relevance_scorer_node,
)

from orchestrator.legacy.ranker import (
    ranker_node,
)


def main():

    state = graph.invoke(
        {
            "query":
                "What is the PTO policy?"
        }
    )

    state = {
        **state,
        **relevance_scorer_node(
            state
        )
    }

    state = {
        **state,
        **ranker_node(
            state
        )
    }

    print("\n")
    print("=" * 100)
    print("RANKED RESULTS")
    print("=" * 100)

    for result in state[
        "ranked_results"
    ]:

        pprint(result)


if __name__ == "__main__":
    main()