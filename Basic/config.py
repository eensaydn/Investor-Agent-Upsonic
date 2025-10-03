"""
Configuration file for Investment Report Generator

This file contains the application's configuration settings.
"""

import os
from pathlib import Path

# API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

# File Paths
BASE_DIR = Path(__file__).parent
REPORTS_DIR = BASE_DIR / "reports" / "investment"

# Report File Names
STOCK_ANALYST_REPORT = "stock_analyst_report.md"
RESEARCH_ANALYST_REPORT = "research_analyst_report.md"
INVESTMENT_REPORT = "investment_report.md"

# Agent Configuration
AGENT_CONFIG = {
    "stock_analyst": {
        "name": "Stock Analyst",
        "role": "Senior Investment Analyst at Goldman Sachs",
        "model": OPENAI_MODEL,
        "temperature": 0.7,
        "max_tokens": 4000
    },
    "research_analyst": {
        "name": "Research Analyst", 
        "role": "Senior Research Analyst at Goldman Sachs",
        "model": OPENAI_MODEL,
        "temperature": 0.7,
        "max_tokens": 4000
    },
    "investment_lead": {
        "name": "Investment Lead",
        "role": "Senior Investment Lead at Goldman Sachs", 
        "model": OPENAI_MODEL,
        "temperature": 0.7,
        "max_tokens": 4000
    }
}

# Example Company Groups
EXAMPLE_COMPANIES = {
    "tech_giants": ["AAPL", "MSFT", "GOOGL"],
    "semiconductor": ["NVDA", "AMD", "INTC"],
    "automotive": ["TSLA", "F", "GM"],
    "banking": ["JPM", "BAC", "GS"],
    "retail": ["AMZN", "WMT", "TGT"],
    "healthcare": ["PFE", "JNJ", "MRNA"],
    "energy": ["XOM", "CVX", "BP"]
}

# Analysis Templates
ANALYSIS_TEMPLATES = {
    "comprehensive": "Generate comprehensive investment analysis and portfolio allocation recommendations",
    "esg_focused": "Focus on ESG factors and sustainable investing principles",
    "growth_focused": "Focus on growth potential and innovation capabilities",
    "value_focused": "Focus on value investing principles and intrinsic value assessment",
    "risk_focused": "Focus on risk assessment and downside protection strategies"
}

# Output Configuration
OUTPUT_CONFIG = {
    "encoding": "utf-8",
    "include_timestamps": True,
    "include_disclaimers": True,
    "markdown_formatting": True
}

# Validation
def validate_config():
    """Validate configuration"""
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY environment variable is required")
    
    if not REPORTS_DIR.exists():
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    return True

# Initialize configuration
if __name__ == "__main__":
    try:
        validate_config()
        print("✅ Configuration validated successfully")
    except Exception as e:
        print(f"❌ Configuration validation failed: {e}")

