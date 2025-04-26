import asyncio
import ollama
from typing import AsyncGenerator

class LLMModel:
    def __init__(self, model_name: str = "deepseek-coder:1.3b", temperature: float = 0.5, top_p: float = 0.95, max_tokens: int = 200):
        self.model_name = model_name
        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_tokens

    async def generate_stream(self, prompt: str) -> AsyncGenerator[str, None]:
        """
        Async generator that streams responses from Ollama.
        """
        response =ollama.chat(
            model=self.model_name,
            #prompt=prompt,
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
            yield chunk['message']['content']
