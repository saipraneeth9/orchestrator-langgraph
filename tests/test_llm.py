from clients.ollama_client import get_ollama_llm

llm = get_ollama_llm()

response = llm.invoke(
    "What is LangGraph?"
)

print(response.content)