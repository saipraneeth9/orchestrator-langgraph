from schemas.answer_type import (
    AnswerType,
)


def classify_by_rules(
    answer: str,
):

    answer = answer.lower()

    # --------------------------------------------------
    # ROOT CAUSE
    # --------------------------------------------------

    root_cause_patterns = [

        "caused by",

        "due to",

        "root cause",

        "investigation showed",

        "investigation found",

        "latency",

        "timeout",

        "failure caused by",

        "issue caused by",

        "problem caused by",

        "because of",

        "triggered by",

        "integration latency",

        "misconfiguration",

        "configuration issue",

        "network issue",

        "database issue",

        "permission issue",
    ]

    if any(

        pattern in answer

        for pattern

        in root_cause_patterns

    ):

        return (
            AnswerType.ROOT_CAUSE
        )

    # --------------------------------------------------
    # PROCESS
    # --------------------------------------------------

    process_patterns = [

        "processed through",

        "workflow",

        "approval process",

        "process",

        "submitted through",

        "approved through",

        "routed through",

        "managers approve",

        "handled by",

        "managed by",

        "follows the process",

        "steps are",

        "procedure",
    ]

    if any(

        pattern in answer

        for pattern

        in process_patterns

    ):

        return (
            AnswerType.PROCESS
        )

    # --------------------------------------------------
    # POLICY
    # --------------------------------------------------

    policy_patterns = [

        "policy",

        "employees receive",

        "employees are entitled",

        "employees may",

        "employees must",

        "required to",

        "according to policy",

        "annual leave",

        "pto days",

        "guideline",

        "standard policy",

        "compliance requirement",
    ]

    if any(

        pattern in answer

        for pattern

        in policy_patterns

    ):

        return (
            AnswerType.POLICY
        )

    # --------------------------------------------------
    # OBSERVATION
    # --------------------------------------------------

    observation_patterns = [

        "users reported",

        "community",

        "employees reported",

        "multiple users",

        "several users",

        "reported intermittent",

        "reported delays",

        "reported failures",

        "reported issues",

        "observed",

        "experience delays",

        "experienced delays",
    ]

    if any(

        pattern in answer

        for pattern

        in observation_patterns

    ):

        return (
            AnswerType.OBSERVATION
        )

    # --------------------------------------------------
    # WORKAROUND
    # --------------------------------------------------

    workaround_patterns = [

        "restart",

        "clear cache",

        "workaround",

        "temporary fix",

        "resolved by",

        "clear cached credentials",

        "restart service",

        "retry request",

        "manual workaround",

        "temporary resolution",
    ]

    if any(

        pattern in answer

        for pattern

        in workaround_patterns

    ):

        return (
            AnswerType.WORKAROUND
        )

    return None