"""Health check API routes."""

from datetime import datetime
from fastapi import APIRouter

from ..models.schemas import HealthResponse
from ...config.settings import settings

router = APIRouter(prefix="/api/v1", tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Health check endpoint."""
    
    return HealthResponse(
        status="healthy",
        version=settings.APP_VERSION,
        timestamp=datetime.now().isoformat()
    )
