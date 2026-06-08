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

from orchestrator.legacy.synthesizer import (
    synthesizer_node,
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

    state.update(
        synthesizer_node(
            state
        )
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


if __name__ == "__main__":
    main()