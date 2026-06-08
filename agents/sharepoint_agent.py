from handlers.sharepoint_handler import (
    SharePointHandler
)

from schemas.agent_output import (
    AgentOutput,
)

from schemas.trace_event import (
    TraceEvent,
)

from utils.tracing import (
    Timer,
)


def sharepoint_agent(state):

    try:

        with Timer() as timer:

            handler = SharePointHandler()

            response = handler.search(
                state["query"]
            )

        return {

            "agent_outputs": [

                AgentOutput(

                    source="sharepoint",

                    response=response,
                )
            ],

            "execution_trace": [

                TraceEvent(

                    node="sharepoint_agent",

                    status="success",

                    duration_ms=round(
                        timer.duration_ms,
                        2
                    ),

                    metadata={
                        "source": "sharepoint",
                    }
                )
            ]
        }

    except Exception as e:

        return {

            "errors": [
                {
                    "node": "sharepoint_agent",
                    "error": str(e),
                }
            ],

            "execution_trace": [

                TraceEvent(

                    node="sharepoint_agent",

                    status="failed",

                    duration_ms=0,

                    metadata={
                        "source": "sharepoint",
                        "error": str(e),
                    }
                )
            ]
        }