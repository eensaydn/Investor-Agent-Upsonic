"""Pydantic models for API requests and responses."""

from typing import List, Optional
from pydantic import BaseModel, Field


class AnalysisRequest(BaseModel):
    """Request model for investment analysis."""
    
    companies: str = Field(
        ..., 
        description="Comma-separated list of company symbols (e.g., 'AAPL, MSFT, GOOGL')",
        example="AAPL, MSFT, GOOGL"
    )
    message: Optional[str] = Field(
        default="Generate comprehensive investment analysis and portfolio allocation recommendations",
        description="Custom analysis message or instructions"
    )


class AnalysisResponse(BaseModel):
    """Response model for investment analysis."""
    
    analysis_id: str = Field(..., description="Unique identifier for the analysis")
    status: str = Field(..., description="Analysis status")
    message: str = Field(..., description="Status message")
    companies: str = Field(..., description="Companies being analyzed")


class StockAnalysisResult(BaseModel):
    """Stock analysis result model."""
    
    company_symbols: str = Field(..., description="Company symbols analyzed")
    market_analysis: str = Field(..., description="Market analysis results")
    financial_metrics: str = Field(..., description="Financial metrics analysis")
    risk_assessment: str = Field(..., description="Risk assessment")
    recommendations: str = Field(..., description="Initial recommendations")


class InvestmentRanking(BaseModel):
    """Investment ranking result model."""
    
    ranked_companies: str = Field(..., description="Companies ranked by investment potential")
    investment_rationale: str = Field(..., description="Investment rationale for each company")
    risk_evaluation: str = Field(..., description="Risk evaluation and mitigation strategies")
    growth_potential: str = Field(..., description="Growth potential assessment")


class PortfolioAllocation(BaseModel):
    """Portfolio allocation result model."""
    
    allocation_strategy: str = Field(..., description="Portfolio allocation strategy")
    investment_thesis: str = Field(..., description="Investment thesis and rationale")
    risk_management: str = Field(..., description="Risk management approach")
    final_recommendations: str = Field(..., description="Final actionable recommendations")


class ReportResponse(BaseModel):
    """Response model for generated reports."""
    
    analysis_id: str = Field(..., description="Analysis identifier")
    status: str = Field(..., description="Report status")
    reports: Optional[dict] = Field(None, description="Generated report files")
    summary: Optional[str] = Field(None, description="Analysis summary")


class HealthResponse(BaseModel):
    """Health check response model."""
    
    status: str = Field(..., description="Service status")
    version: str = Field(..., description="Application version")
    timestamp: str = Field(..., description="Current timestamp")

