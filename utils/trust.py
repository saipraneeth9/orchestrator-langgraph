def get_effective_trust(
    source: str,
    source_trust: list,
    default: float = 0.50,
) -> float:

    for trust in source_trust:
        if trust.source == source:
            return getattr(
                trust,
                "effective_trust",
                default,
            )

    return default


def get_trust_gap(
    primary_source: str,
    supporting_sources: list[str],
    source_trust: list,
) -> float:

    primary_score = get_effective_trust(
        primary_source,
        source_trust,
        0.0,
    )

    if not supporting_sources:
        return round(
            primary_score,
            2,
        )

    highest_competitor = max(
        (
            get_effective_trust(
                source,
                source_trust,
                0.0,
            )
            for source in supporting_sources
        ),
        default=0.0,
    )

    return round(
        primary_score - highest_competitor,
        2,
    )