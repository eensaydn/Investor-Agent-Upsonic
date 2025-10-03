"""Investment Lead Agent - Portfolio allocation and strategy."""

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

from ..api.models.schemas import PortfolioAllocation, InvestmentRanking


class InvestmentLeadAgent:
    """Investment Lead Agent for portfolio strategy and allocation."""
    
    def __init__(self):
        """Initialize the Investment Lead Agent."""
        self.name = "Investment Lead"
        self.description = """
        You are PortfolioSage-X, a distinguished Senior Investment Lead at Goldman Sachs expert in:
        - Portfolio strategy development
        - Asset allocation optimization
        - Risk management
        - Investment rationale articulation
        - Client recommendation delivery
        """
        
        self.instructions = """
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
        """
        
        # Initialize agent
        self.agent = Agent(
            name=self.name,
            model="gpt-4o-mini",
            api_key=os.getenv("OPENAI_API_KEY")
        )
    
    async def analyze(self, investment_ranking: InvestmentRanking) -> PortfolioAllocation:
        """Develop portfolio allocation strategy."""
        
        # Prepare portfolio strategy prompt
        prompt = f"""
        Based on the investment ranking and analysis below, create a strategic portfolio allocation.
        
        INVESTMENT RANKING:
        - Company Rankings: {investment_ranking.ranked_companies}
        - Investment Rationale: {investment_ranking.investment_rationale}
        - Risk Evaluation: {investment_ranking.risk_evaluation}
        - Growth Potential: {investment_ranking.growth_potential}
        
        Please provide:
        1. Specific allocation percentages for each company
        2. Investment thesis and strategic rationale
        3. Risk management approach
        4. Final actionable recommendations
        
        Structure your response with these sections:
        - Allocation Strategy: [Specific percentage allocations and reasoning]
        - Investment Thesis: [Overall investment thesis and strategy]
        - Risk Management: [Risk management approach and mitigation]
        - Final Recommendations: [Actionable recommendations and next steps]
        """
        
        # Get analysis from Upsonic agent
        response = await self.agent.run(prompt)
        
        # Parse response into structured format
        response_text = str(response)
        sections = self._parse_response(response_text)
        
        return PortfolioAllocation(
            allocation_strategy=sections.get("allocation_strategy", response_text[:500]),
            investment_thesis=sections.get("investment_thesis", response_text[500:1000]),
            risk_management=sections.get("risk_management", response_text[1000:1500]),
            final_recommendations=sections.get("final_recommendations", response_text[1500:2000])
        )
    
    def _parse_response(self, response: str) -> Dict[str, str]:
        """Parse agent response into structured sections."""
        sections = {}
        
        # Simple parsing logic
        if "Allocation Strategy:" in response:
            start = response.find("Allocation Strategy:") + len("Allocation Strategy:")
            end = response.find("Investment Thesis:", start)
            if end == -1:
                end = len(response)
            sections["allocation_strategy"] = response[start:end].strip()
        
        if "Investment Thesis:" in response:
            start = response.find("Investment Thesis:") + len("Investment Thesis:")
            end = response.find("Risk Management:", start)
            if end == -1:
                end = len(response)
            sections["investment_thesis"] = response[start:end].strip()
        
        if "Risk Management:" in response:
            start = response.find("Risk Management:") + len("Risk Management:")
            end = response.find("Final Recommendations:", start)
            if end == -1:
                end = len(response)
            sections["risk_management"] = response[start:end].strip()
        
        if "Final Recommendations:" in response:
            start = response.find("Final Recommendations:") + len("Final Recommendations:")
            sections["final_recommendations"] = response[start:].strip()
        
        return sections
