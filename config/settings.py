import os

ROUTER_MODEL = os.getenv(
    "ROUTER_MODEL",
    "qwen2.5-coder:7b"
)

SYNTHESIZER_MODEL = os.getenv(
    "SYNTHESIZER_MODEL",
    "qwen2.5-coder:7b"
)

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)