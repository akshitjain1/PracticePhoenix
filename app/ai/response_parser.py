import json
import re
from typing import Type, TypeVar
from pydantic import BaseModel, ValidationError

from app.ai.schemas.daily_schema import DailyBrief
from app.utils.logger import app_logger

T = TypeVar("T", bound=BaseModel)


class ResponseParser:

    def _clean_text(self, text: str) -> str:
        cleaned = text.strip()
        cleaned = re.sub(
            r"^```json",
            "",
            cleaned,
            flags=re.IGNORECASE
        )
        cleaned = re.sub(
            r"^```",
            "",
            cleaned
        )
        cleaned = re.sub(
            r"```$",
            "",
            cleaned
        )
        return cleaned.strip()

    def parse_section(self, text: str, target_model: Type[T]) -> T:
        cleaned = self._clean_text(text)
        try:
            data = json.loads(cleaned)
        except json.JSONDecodeError as e:
            app_logger.error(f"JSONDecodeError in section {target_model.__name__}: {e}\nRaw Text: {cleaned}")
            raise ValueError(f"Invalid JSON returned by AI for {target_model.__name__}\n\n{e}")

        try:
            return target_model.model_validate(data)
        except ValidationError as e:
            app_logger.error(f"AI response failed validation for {target_model.__name__}:\n{cleaned}")
            raise e

    def parse(self, text: str) -> DailyBrief:
        return self.parse_section(text, DailyBrief)