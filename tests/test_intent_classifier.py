from pprint import pprint

from orchestrator.intent_classifier import (
    intent_classifier_node
)


QUERIES = [

    "What is the PTO policy?",

    "Show incidents related to PTO approvals",

    "VPN timeout after password reset",

    "How do I reconnect GlobalProtect on Mac?",

    "Why are PTO approvals failing?",

    "Why is VPN failing after password resets?",

    "Show incidents related to VPN outages and explain root cause",

]


def main():

    for query in QUERIES:

        print("\n" + "=" * 80)
        print(query)
        print("=" * 80)

        result = intent_classifier_node(
            {
                "query": query
            }
        )

        pprint(result)


if __name__ == "__main__":
    main()