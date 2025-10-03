## 🎯 Features

- **Three-Stage Analysis System**: Comprehensive stock analysis, investment ranking, and portfolio allocation
- **Upsonic Agent Framework**: Secure and high-performance AI agents
- **Real-Time Market Analysis**: OpenAI GPT-4o powered analysis
- **Professional Reporting**: Detailed reports in Markdown format
- **Risk Management**: Comprehensive risk assessment and mitigation strategies

## 🚀 Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd upsonic-investment-analyzer
```

2. **Install required packages:**
```bash
pip install -r requirements.txt
```

3. **Set your OpenAI API key:**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## 📊 Usage

### Basic Usage

```python
from investment_report_generator_upsonic import InvestmentReportGenerator
import asyncio

async def main():
    generator = InvestmentReportGenerator()
    
    result = await generator.analyze_companies(
        companies="AAPL, MSFT, GOOGL",
        analysis_request="Generate comprehensive investment analysis"
    )
    
    print(result)

asyncio.run(main())
```

### Command Line Execution

```bash
python investment_report_generator_upsonic.py
```

## 🏗️ Architecture

### Agent Structure

1. **Stock Analyst (MarketMaster-X)**
   - Market research and financial analysis
   - Risk assessment
   - Industry trend analysis

2. **Research Analyst (ValuePro-X)**
   - Investment opportunity evaluation
   - Company ranking
   - Risk-reward analysis

3. **Investment Lead (PortfolioSage-X)**
   - Portfolio strategy development
   - Asset allocation optimization
   - Final recommendations

### Workflow

```
Input: Company Symbols
    ↓
Phase 1: Stock Analysis
    ↓
Phase 2: Investment Ranking
    ↓
Phase 3: Portfolio Allocation
    ↓
Output: Comprehensive Reports
```

## 📁 Output Files

- `reports/investment/stock_analyst_report.md` - Stock analysis report
- `reports/investment/research_analyst_report.md` - Investment ranking report
- `reports/investment/investment_report.md` - Portfolio allocation report

## 🎯 Example Companies to Analyze

- **Tech Giants**: AAPL, MSFT, GOOGL
- **Semiconductor Leaders**: NVDA, AMD, INTC
- **Automotive Innovation**: TSLA, F, GM
- **Banking Sector**: JPM, BAC, GS
- **Retail Competition**: AMZN, WMT, TGT
- **Healthcare Focus**: PFE, JNJ, MRNA
- **Energy Sector**: XOM, CVX, BP

## ⚠️ Important Notes

- This analysis is for **educational purposes only**
- Should not be used as financial advice
- Consult professional financial advisors before making investment decisions
- OpenAI API usage is paid

## 🔧 Development

### Adding New Agents

```python
def create_custom_analyst():
    return Agent(
        name="Custom Analyst",
        model="openai/gpt-4o",
        role="Your Role",
        goal="Your Goal",
        instructions="Your Instructions"
    )
```

### Adding New Analysis Types

```python
class CustomAnalysisResult(BaseModel):
    custom_field: str
    # Other fields...
```

## 📚 Resources

- [Upsonic Documentation](https://docs.upsonic.ai/)
- [Upsonic GitHub](https://github.com/Upsonic/Upsonic)
- [Agno Investment Report Generator](https://docs.agno.com/examples/use-cases/workflows/investment-report-generator)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🆘 Support

For questions:
- Open GitHub Issues
- Join the Discord community
- Check the documentation


