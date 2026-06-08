from handlers.barnum_handler import (
    BarnumHandler
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


def barnum_agent(state):

    try:

        with Timer() as timer:

            handler = BarnumHandler()

            response = handler.search(
                state["query"]
            )

        return {

            "agent_outputs": [

                AgentOutput(

                    source="barnum",

                    response=response,
                )
            ],

            "execution_trace": [

                TraceEvent(

                    node="barnum_agent",

                    status="success",

                    duration_ms=round(
                        timer.duration_ms,
                        2
                    ),

                    metadata={
                        "source": "barnum",
                    }
                )
            ]
        }

    except Exception as e:

        return {

            "errors": [
                {
                    "node": "barnum_agent",
                    "error": str(e),
                }
            ],

            "execution_trace": [

                TraceEvent(

                    node="barnum_agent",

                    status="failed",

                    duration_ms=0,

                    metadata={
                        "source": "barnum",
                        "error": str(e),
                    }
                )
            ]
        }