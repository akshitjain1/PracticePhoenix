from app.config.settings import settings
from app.ai.providers.groq_provider import GroqProvider


class ProviderFactory:

    @staticmethod
    def get_provider():

        if settings.AI_PROVIDER == "groq":
            return GroqProvider()

        raise ValueError(
            f"Unsupported AI Provider: {settings.AI_PROVIDER}"
        )