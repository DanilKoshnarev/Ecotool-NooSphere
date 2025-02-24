import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import datetime

from src.domain.eco_advice.entities import EcoAdviceRequest
from src.domain.eco_advice.services import EcoAdviceService
from src.infrastructure.ai.openai_service import OpenAIEcoService
from src.infrastructure.persistence.mongodb.eco_advice_repository import MongoEcoAdviceRepository
from src.infrastructure.persistence.mongodb.database import init_mongodb

app = FastAPI()

# Configure templates
templates = Jinja2Templates(directory="src/presentation/web/templates")

@app.on_event("startup")
async def startup_event():
    try:
        await init_mongodb()
    except Exception as e:
        print(f"Failed to initialize MongoDB: {e}")
        raise

# Initialize services
ai_service = OpenAIEcoService(api_key=os.getenv("OPENAI_API_KEY"))
repository = MongoEcoAdviceRepository()
eco_service = EcoAdviceService(ai_service, repository)

class QuestionRequest(BaseModel):
    question: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/advice")
async def get_advice(question_request: QuestionRequest):
    try:
        request = EcoAdviceRequest(
            user_id="anonymous",  # For simplicity, we're using anonymous user
            question=question_request.question
        )
        
        advice = await eco_service.generate_advice(request)
        return advice
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))