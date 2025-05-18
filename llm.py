from langchain_ollama import OllamaLLM

# Create LLM instance with optimized parameters
llm = OllamaLLM(
    model="gemma:latest",
    temperature=0.3,  # Lower temperature for more focused outputs
    top_p=0.8,       # Slightly lower top_p for more deterministic responses
    num_ctx=2048,    # Context window size
    repeat_penalty=1.1,  # Slight penalty for repetition
    num_thread=4,    # Use multiple threads for processing
)
