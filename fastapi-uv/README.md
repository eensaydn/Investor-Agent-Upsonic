# Investment Report Generator

An AI-powered investment analysis system built with Upsonic Agent Framework, FastAPI, and Streamlit.

## Features

- **Multi-Agent Analysis**: Three specialized AI agents for comprehensive investment analysis
- **Real-time Data**: Live market data analysis using DuckDuckGo search
- **Professional Reports**: Detailed markdown reports with analysis and recommendations
- **Modern UI**: Clean Streamlit interface for easy interaction
- **REST API**: FastAPI backend for programmatic access

## Architecture

### Agents
1. **Stock Analyst**: Market research and financial analysis
2. **Research Analyst**: Investment ranking and evaluation
3. **Investment Lead**: Portfolio allocation and strategy

### Tech Stack
- **Framework**: Upsonic Agent Framework
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Package Manager**: UV
- **Language**: Python 3.9+

## Quick Start

### Prerequisites
- Python 3.9+
- UV package manager
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd investor-agent
```

2. Install dependencies with UV:
```bash
uv sync
```

3. Set environment variables:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

### Running the Application

#### Option 1: Streamlit Frontend
```bash
uv run streamlit run src/frontend/app.py
```

#### Option 2: FastAPI Backend
```bash
uv run uvicorn src.api.main:app --reload
```

## Usage

### Web Interface
1. Open the Streamlit app
2. Enter company symbols (e.g., "AAPL, MSFT, GOOGL")
3. Click "Generate Analysis"
4. View and download the generated reports

### API Endpoints
- `POST /analyze`: Start investment analysis
- `GET /reports/{report_id}`: Get analysis results
- `GET /health`: Health check

## Example Companies

- **Tech Giants**: AAPL, MSFT, GOOGL
- **Semiconductors**: NVDA, AMD, INTC
- **Automotive**: TSLA, F, GM
- **Banking**: JPM, BAC, GS
- **Retail**: AMZN, WMT, TGT
- **Healthcare**: PFE, JNJ, MRNA
- **Energy**: XOM, CVX, BP

## Disclaimer

This tool is for educational and research purposes only. It should not be considered as financial advice. Always consult with qualified financial advisors before making investment decisions.

## License

MIT License


