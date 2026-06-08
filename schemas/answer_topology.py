from pydantic import BaseModel


class AnswerTopology(
    BaseModel
):

    source_count: int

    unique_answer_types: int

    complementary_answers: bool

    redundant_answers: bool

    conflicting_answers: bool

    consensus_strength: float