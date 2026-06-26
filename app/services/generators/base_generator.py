from pathlib import Path
from typing import Generic, Type, TypeVar
from pydantic import BaseModel
from app.ai.generator import AIGenerator
from app.ai.response_parser import ResponseParser
from app.utils.logger import app_logger

T = TypeVar("T", bound=BaseModel)
PROMPTS_DIR = Path(__file__).resolve().parents[2] / "ai" / "prompts"


class BaseGenerator(Generic[T]):

    def __init__(self, template_filename: str, target_model: Type[T]):
        self.template_path = PROMPTS_DIR / template_filename
        self.system_path = PROMPTS_DIR / "system.md"
        self.target_model = target_model
        self.ai = AIGenerator()
        self.parser = ResponseParser()

    def _load_prompt(self, **kwargs) -> str:
        system_prompt = self.system_path.read_text(encoding="utf-8").strip()
        template = self.template_path.read_text(encoding="utf-8")
        user_prompt = template.format(**kwargs) if kwargs else template
        return f"{system_prompt}\n\n{user_prompt}"

    def generate(self, fallback_instance: T, **kwargs) -> T:
        prompt = self._load_prompt(**kwargs)
        for attempt in range(3):
            try:
                response = self.ai.generate(prompt)
                return self.parser.parse_section(response, self.target_model)
            except Exception as e:
                app_logger.warning(
                    f"Generator {self.__class__.__name__} attempt {attempt+1} failed: {e}"
                )
        app_logger.error(
            f"Generator {self.__class__.__name__} exhausted retries. Using fallback."
        )
        return fallback_instance
