from typing import Optional
from datetime import datetime
import uuid

from .entities import EcoAdvice, EcoAdviceRequest
from .value_objects import EcoAdviceContent, EcoAdviceMetadata

class EcoAdviceService:
    def __init__(self, ai_service, repository):
        self.ai_service = ai_service
        self.repository = repository

    async def generate_advice(self, request: EcoAdviceRequest) -> EcoAdvice:
        # Generate advice using AI service
        ai_response = await self.ai_service.generate_eco_advice(request.question)
        
        # Create advice content
        content = EcoAdviceContent(
            text=ai_response.text,
            confidence_score=ai_response.confidence,
            tags=ai_response.tags
        )
        
        # Create metadata
        metadata = EcoAdviceMetadata(
            category=ai_response.category,
            environmental_impact_score=ai_response.impact_score,
            implementation_difficulty=ai_response.difficulty,
            estimated_resource_savings=ai_response.savings
        )
        
        # Create advice entity
        advice = EcoAdvice(
            id=str(uuid.uuid4()),
            request_id=request.id,
            content=content.text,
            created_at=datetime.now(),
            metadata=metadata.__dict__
        )
        
        # Save to repository
        await self.repository.save(advice)
        
        return advice