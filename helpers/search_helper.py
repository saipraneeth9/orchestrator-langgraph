import re


STOP_WORDS = {
    "the",
    "is",
    "a",
    "an",
    "of",
    "to",
    "for",
    "in",
    "on",
    "at",
    "and",
    "or",
    "do",
    "does",
    "did",
    "how",
    "what",
    "why",
    "when",
    "where",
    "are",
    "was",
    "were",
    "be",
    "being",
    "been",
    "after",
    "before",
    "with",
    "without",
    "from",
    "by",
    "into",
    "through",
    "about",
    "related",
}


def tokenize(text: str) -> set[str]:
    """
    Normalize text and remove stop words.
    """

    tokens = re.findall(
        r"\b[a-zA-Z0-9]+\b",
        text.lower()
    )

    return {
        token
        for token in tokens
        if token not in STOP_WORDS
    }


def simple_match(
    query: str,
    text: str,
    min_overlap: int = 1,
) -> bool:
    """
    Basic enterprise-friendly token overlap matcher.

    Examples:

    PTO policy
        matches
    PTO approval workflow

    VPN timeout after password reset
        matches
    VPN timeout after password reset

    PTO policy
        does NOT match
    GlobalProtect reconnect issue
    """

    query_tokens = tokenize(query)

    text_tokens = tokenize(text)

    overlap = query_tokens.intersection(
        text_tokens
    )

    return len(overlap) >= min_overlap