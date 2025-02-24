from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class User(BaseModel):
    id: str
    username: str
    created_at: datetime

class EcoAdviceRequest(BaseModel):
    user_id: str
    question: str
    created_at: datetime = datetime.now()

class EcoAdvice(BaseModel):
    id: str
    request_id: str
    content: str
    created_at: datetime
    metadata: Optional[dict] = None