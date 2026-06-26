from groq import Groq
from tenacity import retry, stop_after_attempt, wait_exponential

from app.config.settings import settings
from app.ai.providers.base_provider import BaseProvider


class GroqProvider(BaseProvider):

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=2),
    )
    def generate(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            model=settings.MODEL_NAME,
            temperature=0.2,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ]
        )

        return response.choices[0].message.content