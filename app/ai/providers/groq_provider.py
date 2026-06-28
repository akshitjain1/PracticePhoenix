from groq import Groq
from tenacity import retry, stop_after_attempt, wait_exponential

from app.config.settings import settings
from app.ai.providers.base_provider import BaseProvider
from app.utils.logger import app_logger


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
        try:
            response = self.client.chat.completions.create(
                model=settings.MODEL_NAME,
                temperature=0.2,
                response_format={"type": "json_object"},
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ]
            )
        except Exception as e:
            app_logger.debug(f"Groq json_object mode failed or unsupported ({e}), retrying standard completion.")
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