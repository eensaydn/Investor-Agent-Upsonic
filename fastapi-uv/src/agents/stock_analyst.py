"""Stock Analyst Agent - Market research and financial analysis."""

import os
from typing import Dict, Any

# Custom Agent implementation for investment analysis
class Agent:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Agent')
        self.model = kwargs.get('model', 'gpt-4o-mini')
        self.api_key = kwargs.get('api_key')
    
    async def run(self, prompt):
        # OpenAI API call for analysis
        try:
            from openai import AsyncOpenAI
            client = AsyncOpenAI(api_key=self.api_key)
            
            response = await client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Analysis error: {str(e)}"

from duckduckgo_search import DDGS

from ..api.models.schemas import StockAnalysisResult


class StockAnalystAgent:
    """Stock Analyst Agent for comprehensive market analysis."""
    
    def __init__(self):
        """Initialize the Stock Analyst Agent."""
        self.name = "Stock Analyst"
        self.description = """
        You are MarketMaster-X, an elite Senior Investment Analyst at Goldman Sachs with expertise in:
        - Comprehensive market analysis
        - Financial statement evaluation
        - Industry trend identification
        - News impact assessment
        - Risk factor analysis
        - Growth potential evaluation
        """
        
        self.instructions = """
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
        """
        
        # Initialize agent
        self.agent = Agent(
            name=self.name,
            model="gpt-4o-mini",
            api_key=os.getenv("OPENAI_API_KEY")
        )
    
    def search_company_info(self, company_symbols: str) -> str:
        """Search for company information using DuckDuckGo."""
        try:
            ddgs = DDGS()
            search_results = []
            
            companies = [symbol.strip() for symbol in company_symbols.split(",")]
            
            for company in companies:
                # Search for recent news and financial information
                query = f"{company} stock analysis financial metrics 2024"
                results = ddgs.text(query, max_results=3)
                
                company_info = f"\n--- {company} Information ---\n"
                for result in results:
                    company_info += f"Title: {result.get('title', 'N/A')}\n"
                    company_info += f"Summary: {result.get('body', 'N/A')}\n"
                    company_info += f"Source: {result.get('href', 'N/A')}\n\n"
                
                search_results.append(company_info)
            
            return "\n".join(search_results)
            
        except Exception as e:
            return f"Error searching for company information: {str(e)}"
    
    async def analyze(self, companies: str, message: str) -> StockAnalysisResult:
        """Perform comprehensive stock analysis."""
        
        # Get market data through web search
        market_data = self.search_company_info(companies)
        
        # Prepare analysis prompt
        prompt = f"""
        {message}

        Please conduct a comprehensive analysis of the following companies: {companies}

        Market Data Available:
        {market_data}

        For each company, provide:
        1. Current market position and financial metrics
        2. Recent performance and analyst recommendations
        3. Industry trends and competitive landscape
        4. Risk factors and growth potential
        5. News impact and market sentiment

        Companies to analyze: {companies}
        
        Please structure your response with the following sections:
        - Company Symbols: {companies}
        - Market Analysis: [Detailed market analysis]
        - Financial Metrics: [Key financial metrics and ratios]
        - Risk Assessment: [Risk factors and challenges]
        - Recommendations: [Initial investment recommendations]
        """
        
        # Get analysis from Upsonic agent
        response = await self.agent.run(prompt)
        
        # Parse response into structured format
        # For now, we'll use the full response and structure it
        response_text = str(response)
        
        # Extract sections (simplified parsing)
        sections = self._parse_response(response_text)
        
        return StockAnalysisResult(
            company_symbols=companies,
            market_analysis=sections.get("market_analysis", response_text[:500]),
            financial_metrics=sections.get("financial_metrics", response_text[500:1000]),
            risk_assessment=sections.get("risk_assessment", response_text[1000:1500]),
            recommendations=sections.get("recommendations", response_text[1500:2000])
        )
    
    def _parse_response(self, response: str) -> Dict[str, str]:
        """Parse agent response into structured sections."""
        sections = {}
        
        # Simple parsing logic - in production, this would be more sophisticated
        if "Market Analysis:" in response:
            start = response.find("Market Analysis:") + len("Market Analysis:")
            end = response.find("Financial Metrics:", start)
            if end == -1:
                end = len(response)
            sections["market_analysis"] = response[start:end].strip()
        
        if "Financial Metrics:" in response:
            start = response.find("Financial Metrics:") + len("Financial Metrics:")
            end = response.find("Risk Assessment:", start)
            if end == -1:
                end = len(response)
            sections["financial_metrics"] = response[start:end].strip()
        
        if "Risk Assessment:" in response:
            start = response.find("Risk Assessment:") + len("Risk Assessment:")
            end = response.find("Recommendations:", start)
            if end == -1:
                end = len(response)
            sections["risk_assessment"] = response[start:end].strip()
        
        if "Recommendations:" in response:
            start = response.find("Recommendations:") + len("Recommendations:")
            sections["recommendations"] = response[start:].strip()
        
        return sections
