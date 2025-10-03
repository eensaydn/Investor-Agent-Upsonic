"""Investment analysis workflow orchestrator."""

import asyncio
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

from ..agents.stock_analyst import StockAnalystAgent
from ..agents.research_analyst import ResearchAnalystAgent
from ..agents.investment_lead import InvestmentLeadAgent
from ..api.models.schemas import (
    StockAnalysisResult,
    InvestmentRanking,
    PortfolioAllocation
)
from ..config.settings import settings


class InvestmentWorkflow:
    """Orchestrates the complete investment analysis workflow."""
    
    def __init__(self):
        """Initialize the workflow with all agents."""
        self.stock_analyst = StockAnalystAgent()
        self.research_analyst = ResearchAnalystAgent()
        self.investment_lead = InvestmentLeadAgent()
        
        # Ensure reports directory exists
        self.reports_dir = Path(settings.REPORTS_DIR)
        self.reports_dir.mkdir(exist_ok=True)
    
    async def execute_analysis(
        self, 
        companies: str, 
        message: str = "Generate comprehensive investment analysis and portfolio allocation recommendations"
    ) -> Dict[str, Any]:
        """Execute the complete investment analysis workflow."""
        
        analysis_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        
        print(f"Starting investment analysis for companies: {companies}")
        print(f"Analysis ID: {analysis_id}")
        print(f"Analysis request: {message}")
        
        try:
            # Phase 1: Stock Analysis
            print("\nPHASE 1: COMPREHENSIVE STOCK ANALYSIS")
            print("=" * 60)
            print("Analyzing market data and fundamentals...")
            
            stock_analysis = await self.stock_analyst.analyze(companies, message)
            
            # Save stock analysis report
            stock_report_path = self.reports_dir / f"{analysis_id}_stock_analysis.md"
            await self._save_stock_report(stock_report_path, stock_analysis)
            print(f"Stock analysis completed and saved to {stock_report_path}")
            
            # Phase 2: Investment Ranking
            print("\nPHASE 2: INVESTMENT POTENTIAL RANKING")
            print("=" * 60)
            print("Ranking companies by investment potential...")
            
            investment_ranking = await self.research_analyst.analyze(stock_analysis)
            
            # Save research analysis report
            research_report_path = self.reports_dir / f"{analysis_id}_research_analysis.md"
            await self._save_research_report(research_report_path, investment_ranking)
            print(f"Investment ranking completed and saved to {research_report_path}")
            
            # Phase 3: Portfolio Allocation Strategy
            print("\nPHASE 3: PORTFOLIO ALLOCATION STRATEGY")
            print("=" * 60)
            print("Developing portfolio allocation strategy...")
            
            portfolio_allocation = await self.investment_lead.analyze(investment_ranking)
            
            # Save portfolio strategy report
            portfolio_report_path = self.reports_dir / f"{analysis_id}_portfolio_strategy.md"
            await self._save_portfolio_report(portfolio_report_path, portfolio_allocation)
            print(f"Portfolio strategy completed and saved to {portfolio_report_path}")
            
            # Generate summary
            summary = self._generate_summary(
                analysis_id, companies, stock_analysis, 
                investment_ranking, portfolio_allocation
            )
            
            return {
                "analysis_id": analysis_id,
                "timestamp": timestamp,
                "status": "completed",
                "companies": companies,
                "reports": {
                    "stock_analysis": str(stock_report_path),
                    "research_analysis": str(research_report_path),
                    "portfolio_strategy": str(portfolio_report_path)
                },
                "summary": summary,
                "results": {
                    "stock_analysis": stock_analysis.dict(),
                    "investment_ranking": investment_ranking.dict(),
                    "portfolio_allocation": portfolio_allocation.dict()
                }
            }
            
        except Exception as e:
            error_message = f"Analysis failed: {str(e)}"
            print(f"ERROR: {error_message}")
            
            return {
                "analysis_id": analysis_id,
                "timestamp": timestamp,
                "status": "failed",
                "companies": companies,
                "error": error_message,
                "summary": f"Investment analysis failed for {companies}: {error_message}"
            }
    
    async def _save_stock_report(self, file_path: Path, analysis: StockAnalysisResult) -> None:
        """Save stock analysis report to markdown file."""
        content = f"""# Stock Analysis Report

**Analysis ID:** {file_path.stem}
**Companies:** {analysis.company_symbols}
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Market Analysis
{analysis.market_analysis}

## Financial Metrics
{analysis.financial_metrics}

## Risk Assessment
{analysis.risk_assessment}

## Recommendations
{analysis.recommendations}

---
*This analysis is for educational purposes only and should not be considered as financial advice.*
"""
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    async def _save_research_report(self, file_path: Path, ranking: InvestmentRanking) -> None:
        """Save research analysis report to markdown file."""
        content = f"""# Investment Ranking Report

**Analysis ID:** {file_path.stem}
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Company Rankings
{ranking.ranked_companies}

## Investment Rationale
{ranking.investment_rationale}

## Risk Evaluation
{ranking.risk_evaluation}

## Growth Potential
{ranking.growth_potential}

---
*This analysis is for educational purposes only and should not be considered as financial advice.*
"""
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    async def _save_portfolio_report(self, file_path: Path, allocation: PortfolioAllocation) -> None:
        """Save portfolio strategy report to markdown file."""
        content = f"""# Investment Portfolio Report

**Analysis ID:** {file_path.stem}
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Allocation Strategy
{allocation.allocation_strategy}

## Investment Thesis
{allocation.investment_thesis}

## Risk Management
{allocation.risk_management}

## Final Recommendations
{allocation.final_recommendations}

---
*This analysis is for educational purposes only and should not be considered as financial advice.*
"""
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _generate_summary(
        self, 
        analysis_id: str, 
        companies: str, 
        stock_analysis: StockAnalysisResult,
        investment_ranking: InvestmentRanking,
        portfolio_allocation: PortfolioAllocation
    ) -> str:
        """Generate a summary of the analysis."""
        
        return f"""INVESTMENT ANALYSIS WORKFLOW COMPLETED!

Analysis Summary:
- Analysis ID: {analysis_id}
- Companies Analyzed: {companies}
- Market Analysis: Completed
- Investment Ranking: Completed
- Portfolio Strategy: Completed

Key Insights:
{portfolio_allocation.allocation_strategy[:200]}...

Disclaimer: This analysis is for educational purposes only and should not be considered as financial advice.
"""
