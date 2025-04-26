# llm_model.py

import ollama
from typing import AsyncGenerator

class LLMModel:
    def __init__(self, model_name: str = "deepseek-coder:1.3b", temperature: float = 0.5, top_p: float = 0.95, max_tokens: int = 4096):
        self.model_name = model_name
        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_tokens

    async def generate_stream(self, prompt: str) -> AsyncGenerator[str, None]:
        """
        Async generator that streams responses from Ollama.
        """
        client = ollama.AsyncClient()

        response = await client.chat(
            model=self.model_name,
            messages=[
                {"role": "user", "content": prompt}
            ],
            stream=True,
            options={
                "temperature": self.temperature,
                "top_p": self.top_p,
                "num_predict": self.max_tokens
            }
        )

        async for chunk in response:
            if 'message' in chunk and 'content' in chunk['message']:
                yield chunk['message']['content']
            else:
                continue  # Safety check
