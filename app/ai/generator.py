from app.ai.providers.provider_factory import ProviderFactory


class AIGenerator:

    def __init__(self):

        self.provider = ProviderFactory.get_provider()

    def generate(self, prompt: str):

        return self.provider.generate(prompt)