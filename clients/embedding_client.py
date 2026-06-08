from langchain_ollama import OllamaEmbeddings


class EmbeddingClient:

    _embeddings = None

    @classmethod
    def get_embeddings(cls):

        if cls._embeddings is None:

            cls._embeddings = OllamaEmbeddings(
                model="nomic-embed-text"
            )

        return cls._embeddings

    @classmethod
    def embed_query(
        cls,
        text: str
    ):

        embeddings = cls.get_embeddings()

        return embeddings.embed_query(
            text
        )