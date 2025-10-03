"""Run the FastAPI backend server."""

import uvicorn
from src.config.settings import settings

if __name__ == "__main__":
    print(f"Starting {settings.APP_NAME} API Server")
    print(f"Host: {settings.API_HOST}:{settings.API_PORT}")
    print(f"Debug: {settings.DEBUG}")
    print("API Documentation: http://localhost:8000/docs")
    print("Health Check: http://localhost:8000/api/v1/health")
    
    uvicorn.run(
        "src.api.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG
    )
