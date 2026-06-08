from schemas.response_strategy import (
    ResponseStrategy,
)


def strategy_router(
    state,
):

    strategy = state.get(
        "response_strategy"
    )

    if (
        strategy
        ==
        ResponseStrategy.DIRECT_RESPONSE
    ):
        return "direct_response"

    if (
        strategy
        ==
        ResponseStrategy.CONSOLIDATE
    ):
        return "answer_synthesizer"

    if (
        strategy
        ==
        ResponseStrategy.RESOLVE_CONFLICT
    ):
        return "conflict_resolution"

    return "low_confidence"