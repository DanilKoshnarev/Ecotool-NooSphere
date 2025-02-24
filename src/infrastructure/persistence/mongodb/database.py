from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import os

from .eco_advice_repository import EcoAdviceDocument

async def init_mongodb():
    # Get MongoDB connection details from environment variables
    mongodb_url = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    mongodb_db = os.getenv("MONGODB_DB", "eco_advisor")
    
    # Create Motor client
    client = AsyncIOMotorClient(mongodb_url)
    
    # Initialize Beanie with the document models
    await init_beanie(
        database=client[mongodb_db],
        document_models=[
            EcoAdviceDocument
        ]
    )
    
    return client