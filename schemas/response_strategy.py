from enum import Enum


class ResponseStrategy(
    str,
    Enum,
):

    DIRECT_RESPONSE = (
        "direct_response"
    )

    CONSOLIDATE = (
        "consolidate"
    )

    RESOLVE_CONFLICT = (
        "resolve_conflict"
    )

    LOW_CONFIDENCE = (
        "low_confidence"
    )