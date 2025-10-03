"""Test the investment analysis workflow."""

import asyncio
import os
from src.utils.workflow import InvestmentWorkflow
from src.config.settings import settings

async def test_workflow():
    """Test the complete workflow."""
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("OPENAI_API_KEY environment variable is not set")
        print("Please set it using: export OPENAI_API_KEY='your-api-key'")
        return
    
    print("Testing Investment Analysis Workflow")
    print("=" * 50)
    
    # Initialize workflow
    workflow = InvestmentWorkflow()
    
    # Test with sample companies
    test_companies = "AAPL, MSFT"
    test_message = "Analyze these tech companies for investment potential"
    
    print(f"Testing with companies: {test_companies}")
    print(f"Message: {test_message}")
    print()
    
    try:
        # Run analysis
        result = await workflow.execute_analysis(test_companies, test_message)
        
        print("\nWorkflow Test Results:")
        print(f"Analysis ID: {result['analysis_id']}")
        print(f"Status: {result['status']}")
        print(f"Companies: {result['companies']}")
        
        if result['status'] == 'completed':
            print("\nGenerated Reports:")
            for report_type, file_path in result['reports'].items():
                print(f"  - {report_type}: {file_path}")
            
            print(f"\nSummary:")
            print(result['summary'])
            
        else:
            print(f"Analysis failed: {result.get('error', 'Unknown error')}")
            
    except Exception as e:
        print(f"Test failed with error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_workflow())
