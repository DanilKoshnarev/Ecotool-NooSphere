from typing import Optional
from beanie import Document, PydanticObjectId
from datetime import datetime

from src.domain.eco_advice.entities import EcoAdvice

class EcoAdviceDocument(Document):
    request_id: str
    content: str
    created_at: datetime
    metadata: Optional[dict] = None

    class Settings:
        name = "eco_advice"

class MongoEcoAdviceRepository:
    async def save(self, advice: EcoAdvice) -> None:
        doc = EcoAdviceDocument(
            id=PydanticObjectId(advice.id),
            request_id=advice.request_id,
            content=advice.content,
            created_at=advice.created_at,
            metadata=advice.metadata
        )
        await doc.save()

    async def get_by_id(self, advice_id: str) -> Optional[EcoAdvice]:
        doc = await EcoAdviceDocument.get(PydanticObjectId(advice_id))
        if not doc:
            return None
        
        return EcoAdvice(
            id=str(doc.id),
            request_id=doc.request_id,
            content=doc.content,
            created_at=doc.created_at,
            metadata=doc.metadata
        )