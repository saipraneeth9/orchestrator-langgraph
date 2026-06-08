from handlers.servicenow_handler import (
    ServiceNowHandler
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


def servicenow_agent(state):

    try:

        with Timer() as timer:

            handler = ServiceNowHandler()

            answer = handler.search(
                state["query"]
            )

        return {

            "agent_outputs": [

                AgentOutput(

                    source="servicenow",

                    response=answer,
                )
            ],

            "execution_trace": [

                TraceEvent(

                    node="servicenow_agent",

                    status="success",

                    duration_ms=round(
                        timer.duration_ms,
                        2
                    ),

                    metadata={
                        "source":
                            "servicenow",
                    }
                )
            ]
        }

    except Exception as e:

        return {

            "errors": [
                {
                    "node":
                        "servicenow_agent",
                    "error":
                        str(e),
                }
            ],

            "execution_trace": [

                TraceEvent(

                    node=
                        "servicenow_agent",

                    status=
                        "failed",

                    duration_ms=0,

                    metadata={
                        "source":
                            "servicenow",
                        "error":
                            str(e),
                    }
                )
            ]
        }