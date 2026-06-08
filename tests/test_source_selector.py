from pprint import pprint

from orchestrator.source_selector import (
    source_selector_node
)


def main():

    state = {
        "retrieval_strategy": {
            "search_incidents": True,
            "search_documentation": True,
            "search_community": False,
            "prefer_recall": True,
            "prefer_precision": False,
            "max_sources": 10,
        }
    }

    result = source_selector_node(state)

    pprint(result)


if __name__ == "__main__":
    main()