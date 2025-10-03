"""Analysis API routes."""

import asyncio
from typing import Dict, Any
from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse

from ..models.schemas import AnalysisRequest, AnalysisResponse, ReportResponse
from ...utils.workflow import InvestmentWorkflow
from ...config.settings import settings

router = APIRouter(prefix="/api/v1", tags=["analysis"])

# Store for analysis results (in production, use a proper database)
analysis_store: Dict[str, Dict[str, Any]] = {}

# Initialize workflow
workflow = InvestmentWorkflow()


async def run_analysis_background(analysis_id: str, companies: str, message: str):
    """Run analysis in background and store results."""
    try:
        result = await workflow.execute_analysis(companies, message)
        analysis_store[analysis_id] = result
    except Exception as e:
        analysis_store[analysis_id] = {
            "analysis_id": analysis_id,
            "status": "failed",
            "error": str(e),
            "companies": companies
        }


@router.post("/analyze", response_model=AnalysisResponse)
async def start_analysis(
    request: AnalysisRequest,
    background_tasks: BackgroundTasks
) -> AnalysisResponse:
    """Start investment analysis for given companies."""
    
    # Validate settings
    try:
        settings.validate()
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    # Generate analysis ID
    import uuid
    analysis_id = str(uuid.uuid4())
    
    # Initialize analysis in store
    analysis_store[analysis_id] = {
        "analysis_id": analysis_id,
        "status": "running",
        "companies": request.companies,
        "message": "Analysis in progress..."
    }
    
    # Start background analysis
    background_tasks.add_task(
        run_analysis_background,
        analysis_id,
        request.companies,
        request.message
    )
    
    return AnalysisResponse(
        analysis_id=analysis_id,
        status="started",
        message="Investment analysis has been started. Use the analysis_id to check progress.",
        companies=request.companies
    )


@router.get("/analysis/{analysis_id}", response_model=ReportResponse)
async def get_analysis_result(analysis_id: str) -> ReportResponse:
    """Get analysis results by analysis ID."""
    
    if analysis_id not in analysis_store:
        raise HTTPException(status_code=404, detail="Analysis not found")
    
    result = analysis_store[analysis_id]
    
    return ReportResponse(
        analysis_id=analysis_id,
        status=result.get("status", "unknown"),
        reports=result.get("reports"),
        summary=result.get("summary")
    )


@router.get("/analysis")
async def list_analyses():
    """List all analyses."""
    return {
        "analyses": [
            {
                "analysis_id": aid,
                "status": data.get("status"),
                "companies": data.get("companies"),
                "timestamp": data.get("timestamp")
            }
            for aid, data in analysis_store.items()
        ]
    }


@router.delete("/analysis/{analysis_id}")
async def delete_analysis(analysis_id: str):
    """Delete analysis results."""
    
    if analysis_id not in analysis_store:
        raise HTTPException(status_code=404, detail="Analysis not found")
    
    del analysis_store[analysis_id]
    
    return {"message": f"Analysis {analysis_id} deleted successfully"}
