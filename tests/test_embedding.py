from clients.embedding_client import (
    EmbeddingClient
)


def main():

    vector = EmbeddingClient.embed_query(
        "Why are PTO approvals failing?"
    )

    print(
        f"Embedding length: {len(vector)}"
    )

    print(
        vector[:10]
    )


if __name__ == "__main__":
    main()