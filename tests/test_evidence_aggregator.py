from pprint import pprint

from orchestrator.graph import graph

from orchestrator.legacy.relevance_scorer import (
    relevance_scorer_node,
)

from orchestrator.legacy.ranker import (
    ranker_node,
)

from orchestrator.legacy.evidence_aggregator import (
    evidence_aggregator_node,
)


def main():

    state = graph.invoke(
        {
            "query":
                "Why are PTO approvals failing?"
        }
    )

    state.update(
        relevance_scorer_node(
            state
        )
    )

    state.update(
        ranker_node(
            state
        )
    )

    state.update(
        evidence_aggregator_node(
            state
        )
    )

    print("\n")
    print("=" * 100)
    print("EVIDENCE PACKAGES")
    print("=" * 100)

    for package in state[
        "evidence_packages"
    ]:

        pprint(
            package.model_dump()
        )

    print("\n")
    print("=" * 100)
    print("TOP EVIDENCE")
    print("=" * 100)

    pprint(
        state[
            "evidence_packages"
        ][0].model_dump()
    )


if __name__ == "__main__":
    main()