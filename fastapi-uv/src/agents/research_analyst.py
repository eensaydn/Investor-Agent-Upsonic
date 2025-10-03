"""Research Analyst Agent - Investment ranking and evaluation."""

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

from ..api.models.schemas import InvestmentRanking, StockAnalysisResult


class ResearchAnalystAgent:
    """Research Analyst Agent for investment evaluation and ranking."""
    
    def __init__(self):
        """Initialize the Research Analyst Agent."""
        self.name = "Research Analyst"
        self.description = """
        You are ValuePro-X, an elite Senior Research Analyst at Goldman Sachs specializing in:
        - Investment opportunity evaluation
        - Comparative analysis
        - Risk-reward assessment
        - Growth potential ranking
        - Strategic recommendations
        """
        
        self.instructions = """
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
        """
        
        # Initialize agent
        self.agent = Agent(
            name=self.name,
            model="gpt-4o-mini",
            api_key=os.getenv("OPENAI_API_KEY")
        )
    
    async def analyze(self, stock_analysis: StockAnalysisResult) -> InvestmentRanking:
        """Perform investment ranking and evaluation."""
        
        # Prepare ranking prompt
        prompt = f"""
        Based on the comprehensive stock analysis below, please rank these companies by investment potential.
        
        STOCK ANALYSIS:
        - Companies: {stock_analysis.company_symbols}
        - Market Analysis: {stock_analysis.market_analysis}
        - Financial Metrics: {stock_analysis.financial_metrics}
        - Risk Assessment: {stock_analysis.risk_assessment}
        - Initial Recommendations: {stock_analysis.recommendations}
        
        Please provide:
        1. Detailed ranking of companies from best to worst investment potential
        2. Investment rationale for each company
        3. Risk evaluation and mitigation strategies
        4. Growth potential assessment
        
        Structure your response with these sections:
        - Ranked Companies: [Company ranking with explanations]
        - Investment Rationale: [Detailed rationale for each company]
        - Risk Evaluation: [Risk analysis and mitigation strategies]
        - Growth Potential: [Growth potential assessment]
        """
        
        # Get analysis from Upsonic agent
        response = await self.agent.run(prompt)
        
        # Parse response into structured format
        response_text = str(response)
        sections = self._parse_response(response_text)
        
        return InvestmentRanking(
            ranked_companies=sections.get("ranked_companies", response_text[:500]),
            investment_rationale=sections.get("investment_rationale", response_text[500:1000]),
            risk_evaluation=sections.get("risk_evaluation", response_text[1000:1500]),
            growth_potential=sections.get("growth_potential", response_text[1500:2000])
        )
    
    def _parse_response(self, response: str) -> Dict[str, str]:
        """Parse agent response into structured sections."""
        sections = {}
        
        # Simple parsing logic
        if "Ranked Companies:" in response:
            start = response.find("Ranked Companies:") + len("Ranked Companies:")
            end = response.find("Investment Rationale:", start)
            if end == -1:
                end = len(response)
            sections["ranked_companies"] = response[start:end].strip()
        
        if "Investment Rationale:" in response:
            start = response.find("Investment Rationale:") + len("Investment Rationale:")
            end = response.find("Risk Evaluation:", start)
            if end == -1:
                end = len(response)
            sections["investment_rationale"] = response[start:end].strip()
        
        if "Risk Evaluation:" in response:
            start = response.find("Risk Evaluation:") + len("Risk Evaluation:")
            end = response.find("Growth Potential:", start)
            if end == -1:
                end = len(response)
            sections["risk_evaluation"] = response[start:end].strip()
        
        if "Growth Potential:" in response:
            start = response.find("Growth Potential:") + len("Growth Potential:")
            sections["growth_potential"] = response[start:].strip()
        
        return sections
