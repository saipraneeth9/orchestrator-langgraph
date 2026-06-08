from handlers.confluence_handler import (
    ConfluenceHandler
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


def confluence_agent(state):

    try:

        with Timer() as timer:

            handler = ConfluenceHandler()

            response = handler.search(
                state["query"]
            )

        return {

            "agent_outputs": [

                AgentOutput(

                    source="confluence",

                    response=response,
                )
            ],

            "execution_trace": [

                TraceEvent(

                    node="confluence_agent",

                    status="success",

                    duration_ms=round(
                        timer.duration_ms,
                        2
                    ),

                    metadata={
                        "source": "confluence",
                    }
                )
            ]
        }

    except Exception as e:

        return {

            "errors": [
                {
                    "node": "confluence_agent",
                    "error": str(e),
                }
            ],

            "execution_trace": [

                TraceEvent(

                    node="confluence_agent",

                    status="failed",

                    duration_ms=0,

                    metadata={
                        "source": "confluence",
                        "error": str(e),
                    }
                )
            ]
        }