from enum import Enum


class AnswerType(str, Enum):

    ROOT_CAUSE = "root_cause"

    PROCESS = "process"

    POLICY = "policy"

    OBSERVATION = "observation"

    WORKAROUND = "workaround"

    UNKNOWN = "unknown"