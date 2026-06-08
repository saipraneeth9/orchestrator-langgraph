from config.source_registry import (
    SOURCE_REGISTRY
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.tracing import (
    Timer,
)


def source_selector_node(state):

    strategy = state["retrieval_strategy"]

    with Timer() as timer:

        selected_sources = []

        if strategy["search_incidents"]:

            for source, metadata in SOURCE_REGISTRY.items():

                if "incidents" in metadata["capabilities"]:

                    selected_sources.append(
                        {
                            "source": source,
                            "authority_score":
                                metadata["authority"],
                            "reasoning":
                                "Provides incident information",
                        }
                    )

        if strategy["search_documentation"]:

            for source, metadata in SOURCE_REGISTRY.items():

                if "documentation" in metadata["capabilities"]:

                    selected_sources.append(
                        {
                            "source": source,
                            "authority_score":
                                metadata["authority"],
                            "reasoning":
                                "Provides documentation",
                        }
                    )

        if strategy["search_community"]:

            for source, metadata in SOURCE_REGISTRY.items():

                if "community" in metadata["capabilities"]:

                    selected_sources.append(
                        {
                            "source": source,
                            "authority_score":
                                metadata["authority"],
                            "reasoning":
                                "Provides community knowledge",
                        }
                    )

        unique_sources = {}

        for source in selected_sources:

            unique_sources[
                source["source"]
            ] = source

        selected_source_list = list(
        unique_sources.values()
        )

        selected_source_names = [
            source["source"]
            for source in selected_source_list
        ]

    return {

    "source_selection_result": {

        "sources": selected_source_list,

        "selected_source_names": selected_source_names,

        "reasoning":
            "Capability based selection",
    },

    "execution_trace": [
        TraceEvent(
            node="source_selector",
            status="success",
            duration_ms=round(
                timer.duration_ms,
                2
            ),
            metadata={
                "selected_sources":
                    selected_source_names,
            }
        )
    ]
}