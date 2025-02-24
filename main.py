import asyncio
import uvicorn
from src.presentation.web.app import app
from src.infrastructure.persistence.mongodb.database import init_mongodb

async def startup():
    # Initialize MongoDB connection
    await init_mongodb()

if __name__ == "__main__":
    # Run startup tasks
    asyncio.run(startup())
    
    # Run the FastAPI application
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True
    )