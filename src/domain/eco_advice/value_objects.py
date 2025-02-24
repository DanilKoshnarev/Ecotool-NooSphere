from dataclasses import dataclass
from typing import Optional

@dataclass
class EcoAdviceContent:
    text: str
    confidence_score: Optional[float] = None
    source: Optional[str] = None
    tags: list[str] = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []

@dataclass
class EcoAdviceMetadata:
    category: str
    environmental_impact_score: Optional[float] = None
    implementation_difficulty: Optional[str] = None
    estimated_resource_savings: Optional[dict] = None