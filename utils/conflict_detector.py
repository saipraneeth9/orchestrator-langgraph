from collections import (
    defaultdict,
)

from config.source_registry import (
    SOURCE_REGISTRY,
)

from clients.embedding_client import (
    EmbeddingClient,
)

from helpers.similarity_helper import (
    cosine_similarity,
)

from schemas.conflict_analysis import (
    ConflictAnalysis,
)


CONSENSUS_THRESHOLD = 0.75


def analyze_conflicts(
    responses,
):

    if len(responses) <= 1:

        authority = 0.5

        if responses:

            authority = (
                SOURCE_REGISTRY
                .get(
                    responses[0].source,
                    {}
                )
                .get(
                    "authority",
                    0.5
                )
            )

        return ConflictAnalysis(

            conflict_detected=False,

            consensus_score=1.0,

            confidence_score=
                round(
                    authority,
                    2
                ),

            minimum_similarity=1.0,

            average_similarity=1.0,
        )

    groups = defaultdict(
        list
    )

    for response in responses:

        groups[
            response.answer_type
        ].append(
            response
        )

    similarities = []

    authority_scores = []

    for response in responses:

        authority_scores.append(

            SOURCE_REGISTRY
            .get(
                response.source,
                {}
            )
            .get(
                "authority",
                0.5
            )
        )

    for group_responses in (
        groups.values()
    ):

        if (
            len(group_responses)
            < 2
        ):
            continue

        embeddings = []

        for response in (
            group_responses
        ):

            embeddings.append(

                EmbeddingClient
                .embed_query(
                    response.answer
                )
            )

        for i in range(
            len(embeddings)
        ):

            for j in range(
                i + 1,
                len(embeddings)
            ):

                similarity = (
                    cosine_similarity(
                        embeddings[i],
                        embeddings[j],
                    )
                )

                similarities.append(
                    similarity
                )

    if not similarities:

        average_authority = (

            sum(
                authority_scores
            )

            /

            len(
                authority_scores
            )
        )

        confidence_score = round(

            average_authority,

            2,
        )

        return ConflictAnalysis(

            conflict_detected=False,

            consensus_score=1.0,

            confidence_score=
                confidence_score,

            minimum_similarity=1.0,

            average_similarity=1.0,
        )

    average_similarity = (

        sum(similarities)

        /

        len(similarities)
    )

    minimum_similarity = min(
        similarities
    )

    average_authority = (

        sum(
            authority_scores
        )

        /

        len(
            authority_scores
        )
    )

    confidence_score = round(

        (
            average_similarity
            * average_authority
        ),

        2,
    )

    conflict_detected = (

        average_similarity
        < CONSENSUS_THRESHOLD
    )

    return ConflictAnalysis(

        conflict_detected=
            conflict_detected,

        consensus_score=
            round(
                average_similarity,
                2
            ),

        confidence_score=
            confidence_score,

        minimum_similarity=
            round(
                minimum_similarity,
                2
            ),

        average_similarity=
            round(
                average_similarity,
                2
            ),
    )