from langgraph.constants import Send


def retrieval_router(state):
    """
    Dynamic fan-out router.

    Converts selected sources into LangGraph Send
    instructions so retrieval agents can execute
    in parallel.
    """

    selected_sources = state[
        "source_selection_result"
    ][
        "selected_source_names"
    ]

    sends = []

    source_to_node = {

        "servicenow":
            "servicenow_agent",

        "sharepoint":
            "sharepoint_agent",

        "confluence":
            "confluence_agent",

        "barnum":
            "barnum_agent",
    }

    for source in selected_sources:

        node_name = source_to_node.get(
            source
        )

        if node_name:

            sends.append(
                Send(
                    node_name,
                    state,
                )
            )

    return sends