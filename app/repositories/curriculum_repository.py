import json
from pathlib import Path
from typing import List, Dict
from app.curriculum.schemas import TopicAsset
from app.utils.logger import app_logger

ASSETS_DIR = Path(__file__).resolve().parents[2] / "curriculum"


class CurriculumRepository:

    def __init__(self):
        self._cache: Dict[str, List[TopicAsset]] = {}

    def load_category(self, category: str) -> List[TopicAsset]:
        if category in self._cache:
            return self._cache[category]

        file_path = ASSETS_DIR / f"{category}.json"
        if not file_path.exists():
            raise FileNotFoundError(f"Curriculum asset not found: {file_path}")

        try:
            raw_data = json.loads(file_path.read_text(encoding="utf-8"))
            assets = [TopicAsset.model_validate(item) for item in raw_data]
            self._cache[category] = assets
            return assets
        except Exception as e:
            app_logger.error(f"Failed to load curriculum category {category}: {e}")
            raise ValueError(f"Invalid schema in asset {category}.json: {e}")

    def get_topic_by_index(self, category: str, index: int) -> TopicAsset:
        assets = self.load_category(category)
        if not assets:
            raise ValueError(f"Category {category} is empty.")
        return assets[index % len(assets)]
