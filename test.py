import ollama

response = ollama.chat(
    model="deepseek-coder:1.3b",
    messages=[{"role": "user", "content": "What is the purpose of a function in Python?"}],
     options={"temperature": 0.7, "max_tokens":150}
)

print(response)
