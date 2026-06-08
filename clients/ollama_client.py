from langchain_ollama import ChatOllama

from config.settings import (
    ROUTER_MODEL,
    SYNTHESIZER_MODEL,
    OLLAMA_BASE_URL,
)


class LLMFactory:

    @staticmethod
    def get_router_llm():

        return ChatOllama(
            model=ROUTER_MODEL,
            base_url=OLLAMA_BASE_URL,
            temperature=0,
        )

    @staticmethod
    def get_synthesizer_llm():

        return ChatOllama(
            model=SYNTHESIZER_MODEL,
            base_url=OLLAMA_BASE_URL,
            temperature=0,
        )