"""
💰 Investment Report Generator - Upsonic Agent Implementation

This advanced example demonstrates how to build a sophisticated investment analysis system using the Upsonic agent framework.
The system uses a three-stage approach:
1. Comprehensive stock analysis and market research
2. Investment potential evaluation and ranking
3. Strategic portfolio allocation recommendations

Key capabilities:
- Real-time market data analysis
- Professional financial research
- Investment risk assessment
- Portfolio allocation strategy
- Detailed investment rationale

Example companies to analyze:
- "AAPL, MSFT, GOOGL" (Tech Giants)
- "NVDA, AMD, INTC" (Semiconductor Leaders)
- "TSLA, F, GM" (Automotive Innovation)
- "JPM, BAC, GS" (Banking Sector)
- "AMZN, WMT, TGT" (Retail Competition)
- "PFE, JNJ, MRNA" (Healthcare Focus)
- "XOM, CVX, BP" (Energy Sector)

Installation: pip install upsonic
"""

import asyncio
import random
from pathlib import Path
from shutil import rmtree
from typing import List, Dict, Any
from pydantic import BaseModel

from upsonic import Task, Agent
from upsonic.team import Team

# --- Response Models ---
class StockAnalysisResult(BaseModel):
    company_symbols: str
    market_analysis: str
    financial_metrics: str
    risk_assessment: str
    recommendations: str


class InvestmentRanking(BaseModel):
    ranked_companies: str
    investment_rationale: str
    risk_evaluation: str
    growth_potential: str


class PortfolioAllocation(BaseModel):
    allocation_strategy: str
    investment_thesis: str
    risk_management: str
    final_recommendations: str


# --- File Management ---
reports_dir = Path("reports/investment")
if reports_dir.is_dir():
    rmtree(path=reports_dir, ignore_errors=True)
reports_dir.mkdir(parents=True, exist_ok=True)

stock_analyst_report = str(reports_dir.joinpath("stock_analyst_report.md"))
research_analyst_report = str(reports_dir.joinpath("research_analyst_report.md"))
investment_report = str(reports_dir.joinpath("investment_report.md"))


# --- Agent Definitions ---
def create_stock_analyst():
    """Creates the stock analyst agent"""
    return Agent(
        name="Stock Analyst",
        model="openai/gpt-4o",
        role="Senior Investment Analyst at Goldman Sachs",
        goal="Comprehensive market analysis and financial evaluation",
        instructions="""
        You are MarketMaster-X, an elite Senior Investment Analyst at Goldman Sachs with expertise in:

        - Comprehensive market analysis
        - Financial statement evaluation
        - Industry trend identification
        - News impact assessment
        - Risk factor analysis
        - Growth potential evaluation

        Your tasks:
        1. Market Research 📊
           - Analyze company fundamentals and metrics
           - Review recent market performance
           - Evaluate competitive positioning
           - Assess industry trends and dynamics
        
        2. Financial Analysis 💹
           - Examine key financial ratios
           - Review analyst recommendations
           - Analyze recent news impact
           - Identify growth catalysts
        
        3. Risk Assessment 🎯
           - Evaluate market risks
           - Assess company-specific challenges
           - Consider macroeconomic factors
           - Identify potential red flags

        Note: This analysis is for educational purposes only.
        """,
        education="MBA in Finance, CFA Charterholder",
        work_experience="15+ years in investment banking and equity research"
    )


def create_research_analyst():
    """Creates the research analyst agent"""
    return Agent(
        name="Research Analyst",
        model="openai/gpt-4o",
        role="Senior Research Analyst at Goldman Sachs",
        goal="Investment opportunity evaluation and ranking",
        instructions="""
        You are ValuePro-X, an elite Senior Research Analyst at Goldman Sachs specializing in:

        - Investment opportunity evaluation
        - Comparative analysis
        - Risk-reward assessment
        - Growth potential ranking
        - Strategic recommendations

        Your tasks:
        1. Investment Analysis 🔍
           - Evaluate each company's potential
           - Compare relative valuations
           - Assess competitive advantages
           - Consider market positioning
        
        2. Risk Evaluation 📈
           - Analyze risk factors
           - Consider market conditions
           - Evaluate growth sustainability
           - Assess management capability
        
        3. Company Ranking 🏆
           - Rank based on investment potential
           - Provide detailed rationale
           - Consider risk-adjusted returns
           - Explain competitive advantages
        """,
        education="PhD in Economics, CFA Charterholder",
        work_experience="12+ years in equity research and portfolio management"
    )


def create_investment_lead():
    """Creates the investment lead agent"""
    return Agent(
        name="Investment Lead",
        model="openai/gpt-4o",
        role="Senior Investment Lead at Goldman Sachs",
        goal="Portfolio strategy development and allocation optimization",
        instructions="""
        You are PortfolioSage-X, a distinguished Senior Investment Lead at Goldman Sachs expert in:

        - Portfolio strategy development
        - Asset allocation optimization
        - Risk management
        - Investment rationale articulation
        - Client recommendation delivery

        Your tasks:
        1. Portfolio Strategy 💼
           - Develop allocation strategy
           - Optimize risk-reward balance
           - Consider diversification
           - Set investment timeframes
        
        2. Investment Rationale 📝
           - Explain allocation decisions
           - Support with analysis
           - Address potential concerns
           - Highlight growth catalysts
        
        3. Recommendation Delivery 📊
           - Present clear allocations
           - Explain investment thesis
           - Provide actionable insights
           - Include risk considerations
        """,
        education="MBA in Finance, CFP, CFA Charterholder",
        work_experience="20+ years in portfolio management and investment strategy"
    )


# --- Investment Analysis Workflow ---
class InvestmentReportGenerator:
    """Investment report generator using Upsonic agents"""
    
    def __init__(self):
        self.stock_analyst = create_stock_analyst()
        self.research_analyst = create_research_analyst()
        self.investment_lead = create_investment_lead()
        
        # # Create team
        self.team = Team(
            agents=[self.stock_analyst, self.research_analyst, self.investment_lead],
            mode="sequential"
        )
    
    async def analyze_companies(self, companies: str, analysis_request: str = "Generate comprehensive investment analysis"):
        """Analyze companies and create investment report"""
        
        print(f"🚀 Starting investment analysis for companies: {companies}")
        print(f"💼 Analysis request: {analysis_request}")
        
        # Phase 1: Stock Analysis
        print("\n📊 PHASE 1: COMPREHENSIVE STOCK ANALYSIS")
        print("=" * 60)
        
        stock_analysis_task = Task(
            description=f"""
            {analysis_request}

            Please conduct a comprehensive analysis of the following companies: {companies}

            For each company, provide:
            1. Current market position and financial metrics
            2. Recent performance and analyst recommendations
            3. Industry trends and competitive landscape
            4. Risk factors and growth potential
            5. News impact and market sentiment
            
            Companies to analyze: {companies}
            """,
            response_format=StockAnalysisResult
        )
        
        print("🔍 Analyzing market data and fundamentals...")
        stock_analysis_result = await self.stock_analyst.do_async(stock_analysis_task)
        
        # Save to file
        with open(stock_analyst_report, "w", encoding="utf-8") as f:
            f.write("# Stock Analysis Report\n\n")
            f.write(f"**Companies:** {stock_analysis_result.company_symbols}\n\n")
            f.write(f"## Market Analysis\n{stock_analysis_result.market_analysis}\n\n")
            f.write(f"## Financial Metrics\n{stock_analysis_result.financial_metrics}\n\n")
            f.write(f"## Risk Assessment\n{stock_analysis_result.risk_assessment}\n\n")
            f.write(f"## Recommendations\n{stock_analysis_result.recommendations}\n")
        
        print(f"✅ Stock analysis completed and saved to {stock_analyst_report}")
        
        # Phase 2: Investment Ranking
        print("\n🏆 PHASE 2: INVESTMENT POTENTIAL RANKING")
        print("=" * 60)
        
        ranking_task = Task(
            description=f"""
            Based on the comprehensive stock analysis below, please rank these companies by investment potential.
            
            STOCK ANALYSIS:
            - Market Analysis: {stock_analysis_result.market_analysis}
            - Financial Metrics: {stock_analysis_result.financial_metrics}
            - Risk Assessment: {stock_analysis_result.risk_assessment}
            - Initial Recommendations: {stock_analysis_result.recommendations}
            
            Please provide:
            1. Detailed ranking of companies from best to worst investment potential
            2. Investment rationale for each company
            3. Risk evaluation and mitigation strategies
            4. Growth potential assessment
            """,
            response_format=InvestmentRanking
        )
        
        print("📈 Ranking companies by investment potential...")
        ranking_result = await self.research_analyst.do_async(ranking_task)
        
        # Save to file
        with open(research_analyst_report, "w", encoding="utf-8") as f:
            f.write("# Investment Ranking Report\n\n")
            f.write(f"## Company Rankings\n{ranking_result.ranked_companies}\n\n")
            f.write(f"## Investment Rationale\n{ranking_result.investment_rationale}\n\n")
            f.write(f"## Risk Evaluation\n{ranking_result.risk_evaluation}\n\n")
            f.write(f"## Growth Potential\n{ranking_result.growth_potential}\n")
        
        print(f"✅ Investment ranking completed and saved to {research_analyst_report}")
        
        # Phase 3: Portfolio Allocation Strategy
        print("\n💼 PHASE 3: PORTFOLIO ALLOCATION STRATEGY")
        print("=" * 60)
        
        portfolio_task = Task(
            description=f"""
            Based on the investment ranking and analysis below, create a strategic portfolio allocation.
            
            INVESTMENT RANKING:
            - Company Rankings: {ranking_result.ranked_companies}
            - Investment Rationale: {ranking_result.investment_rationale}
            - Risk Evaluation: {ranking_result.risk_evaluation}
            - Growth Potential: {ranking_result.growth_potential}
            
            Please provide:
            1. Specific allocation percentages for each company
            2. Investment thesis and strategic rationale
            3. Risk management approach
            4. Final actionable recommendations
            """,
            response_format=PortfolioAllocation
        )
        
        print("💰 Developing portfolio allocation strategy...")
        portfolio_result = await self.investment_lead.do_async(portfolio_task)
        
        # Save to file
        with open(investment_report, "w", encoding="utf-8") as f:
            f.write("# Investment Portfolio Report\n\n")
            f.write(f"## Allocation Strategy\n{portfolio_result.allocation_strategy}\n\n")
            f.write(f"## Investment Thesis\n{portfolio_result.investment_thesis}\n\n")
            f.write(f"## Risk Management\n{portfolio_result.risk_management}\n\n")
            f.write(f"## Final Recommendations\n{portfolio_result.final_recommendations}\n")
        
        print(f"✅ Portfolio strategy completed and saved to {investment_report}")
        
        # Final summary
        summary = f"""
        🎉 INVESTMENT ANALYSIS WORKFLOW COMPLETED!

        📊 Analysis Summary:
        • Companies Analyzed: {companies}
        • Market Analysis: ✅ Completed
        • Investment Ranking: ✅ Completed
        • Portfolio Strategy: ✅ Completed

        📁 Reports Generated:
        • Stock Analysis: {stock_analyst_report}
        • Investment Ranking: {research_analyst_report}
        • Portfolio Strategy: {investment_report}

        💡 Key Insights:
        {portfolio_result.allocation_strategy[:200]}...

        ⚠️ Disclaimer: This analysis is for educational purposes only and should not be considered as financial advice.
        """
        
        return summary


# --- Main Execution ---
async def main():
    """Main execution function"""
    
    # Example investment scenarios
    example_scenarios = [
        "AAPL, MSFT, GOOGL",  # Tech Giants
        "NVDA, AMD, INTC",    # Semiconductor Leaders
        "TSLA, F, GM",        # Automotive Innovation
        "JPM, BAC, GS",       # Banking Sector
        "AMZN, WMT, TGT",     # Retail Competition
        "PFE, JNJ, MRNA",     # Healthcare Focus
        "XOM, CVX, BP",       # Energy Sector
    ]
    
    # Get company symbols from user
    print("🧪 Testing Investment Report Generator with Upsonic Framework")
    print("=" * 70)
    
    companies = input(
        "Enter company symbols (comma-separated) "
        "(or press Enter for a suggested portfolio): "
    ).strip()
    
    if not companies:
        companies = random.choice(example_scenarios)
        print(f"✨ Using suggested portfolio: {companies}")
    
    # Create and run Investment Report Generator
    generator = InvestmentReportGenerator()
    
    try:
        result = await generator.analyze_companies(
            companies=companies,
            analysis_request="Generate comprehensive investment analysis and portfolio allocation recommendations"
        )
        
        print("\n" + "="*70)
        print(result)
        
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        print("Please check your OpenAI API key and try again.")


if __name__ == "__main__":
    asyncio.run(main())

