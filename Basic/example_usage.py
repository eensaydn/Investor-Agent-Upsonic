"""
Investment Report Generator - Example Usage

This file demonstrates how to use the Upsonic Investment Report Generator.
"""

import asyncio
from investment_report_generator_upsonic import InvestmentReportGenerator


async def example_basic_usage():
    """Basic usage example"""
    print("🚀 Basic Usage Example")
    print("=" * 50)
    
    # Create generator
    generator = InvestmentReportGenerator()
    
    # Analyze technology companies
    result = await generator.analyze_companies(
        companies="AAPL, MSFT, GOOGL",
        analysis_request="Generate comprehensive investment analysis for tech giants"
    )
    
    print(result)


async def example_custom_analysis():
    """Custom analysis example"""
    print("\n🔍 Custom Analysis Example")
    print("=" * 50)
    
    generator = InvestmentReportGenerator()
    
    # Energy sector analysis
    result = await generator.analyze_companies(
        companies="XOM, CVX, BP",
        analysis_request="Focus on ESG factors and renewable energy transition"
    )
    
    print(result)


async def example_healthcare_sector():
    """Healthcare sector analysis example"""
    print("\n🏥 Healthcare Sector Analysis Example")
    print("=" * 50)
    
    generator = InvestmentReportGenerator()
    
    # Analyze healthcare companies
    result = await generator.analyze_companies(
        companies="PFE, JNJ, MRNA",
        analysis_request="Analyze pharmaceutical companies with focus on innovation and regulatory environment"
    )
    
    print(result)


async def example_sequential_analysis():
    """Sequential analysis example - multiple sectors"""
    print("\n📈 Sequential Analysis Example")
    print("=" * 50)
    
    generator = InvestmentReportGenerator()
    
    sectors = [
        ("AAPL, MSFT, GOOGL", "Technology sector analysis"),
        ("JPM, BAC, GS", "Banking sector analysis"),
        ("AMZN, WMT, TGT", "Retail sector analysis")
    ]
    
    for companies, description in sectors:
        print(f"\n🔍 Analyzing: {companies}")
        print(f"Focus: {description}")
        
        result = await generator.analyze_companies(
            companies=companies,
            analysis_request=description
        )
        
        print(f"✅ Analysis completed for {companies}")


async def main():
    """Main function - run all examples"""
    print("💰 Investment Report Generator - Example Usage")
    print("=" * 60)
    
    try:
        # Basic usage
        await example_basic_usage()
        
        # Custom analysis
        await example_custom_analysis()
        
        # Healthcare sector
        await example_healthcare_sector()
        
        # Sequential analysis
        await example_sequential_analysis()
        
        print("\n🎉 All examples completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during execution: {e}")
        print("Please check your OpenAI API key and try again.")


if __name__ == "__main__":
    asyncio.run(main())

