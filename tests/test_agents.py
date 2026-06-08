from pprint import pprint

from agents.sharepoint_agent import (
    sharepoint_agent,
)

from agents.servicenow_agent import (
    servicenow_agent,
)

from agents.confluence_agent import (
    confluence_agent,
)

from agents.barnum_agent import (
    barnum_agent,
)


TEST_QUERIES = [

    "What is the PTO policy?",

    "VPN timeout after password reset",

    "How do I reconnect GlobalProtect on Mac?",

    "Why are PTO approvals failing?",
]


def run_agent(
    agent_name: str,
    agent_func,
    query: str,
):

    print("\n" + "=" * 100)
    print(f"AGENT: {agent_name}")
    print(f"QUERY: {query}")
    print("=" * 100)

    result = agent_func(
        {
            "query": query,
            "retrieval_results": [],
            "execution_trace": [],
            "errors": [],
        }
    )

    pprint(result)

    print(
        f"\nRetrieved Results: "
        f"{len(result.get('retrieval_results', []))}"
    )


def main():

    agents = [

        (
            "SharePoint",
            sharepoint_agent,
        ),

        (
            "ServiceNow",
            servicenow_agent,
        ),

        (
            "Confluence",
            confluence_agent,
        ),

        (
            "Barnum",
            barnum_agent,
        ),
    ]

    for query in TEST_QUERIES:

        print("\n")
        print("#" * 120)
        print(f"QUERY: {query}")
        print("#" * 120)

        for agent_name, agent_func in agents:

            run_agent(
                agent_name,
                agent_func,
                query,
            )


if __name__ == "__main__":
    main()