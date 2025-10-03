"""Streamlit frontend for Investment Report Generator."""

import streamlit as st
import requests
import time
import json
from pathlib import Path
from typing import Dict, Any, Optional

# Page configuration
st.set_page_config(
    page_title="Investment Report Generator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuration
API_BASE_URL = "http://localhost:8001/api/v1"
REPORTS_DIR = Path("reports")

# Custom CSS
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Header Styles */
    .main-header {
        font-family: 'Inter', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .sub-header {
        font-family: 'Inter', sans-serif;
        font-size: 1.3rem;
        font-weight: 400;
        text-align: center;
        color: #64748b;
        margin-bottom: 3rem;
        opacity: 0.9;
    }
    
    /* Card Styles */
    .analysis-card {
        background: linear-gradient(145deg, #ffffff 0%, #f8fafc 100%);
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        border: 1px solid rgba(226, 232, 240, 0.8);
        margin-bottom: 2rem;
    }
    
    /* Status Boxes */
    .status-box {
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    .status-running {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border: 1px solid #f59e0b;
        color: #92400e;
    }
    
    .status-completed {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border: 1px solid #10b981;
        color: #065f46;
    }
    
    .status-failed {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border: 1px solid #ef4444;
        color: #991b1b;
    }
    
    /* Example Cards */
    .company-example {
        background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #3b82f6;
        margin: 1rem 0;
        font-family: 'Inter', sans-serif;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Form Styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border-radius: 8px;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(59, 130, 246, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(59, 130, 246, 0.4);
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        margin-top: 3rem;
        padding: 2rem;
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border-radius: 12px;
        font-family: 'Inter', sans-serif;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2.5rem;
        }
        
        .analysis-card {
            padding: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)


def check_api_health() -> bool:
    """Check if API is running."""
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        return response.status_code == 200
    except:
        return False


def start_analysis(companies: str, message: str) -> Optional[str]:
    """Start investment analysis."""
    try:
        response = requests.post(
            f"{API_BASE_URL}/analyze",
            json={"companies": companies, "message": message},
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()["analysis_id"]
        else:
            st.error(f"Failed to start analysis: {response.text}")
            return None
            
    except Exception as e:
        st.error(f"Error starting analysis: {str(e)}")
        return None


def get_analysis_result(analysis_id: str) -> Optional[Dict[str, Any]]:
    """Get analysis results."""
    try:
        response = requests.get(f"{API_BASE_URL}/analysis/{analysis_id}", timeout=10)
        
        if response.status_code == 200:
            return response.json()
        else:
            return None
            
    except Exception as e:
        st.error(f"Error getting analysis result: {str(e)}")
        return None


def display_report_content(file_path: str) -> None:
    """Display report content from file."""
    try:
        path = Path(file_path)
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            st.markdown(content)
        else:
            st.warning(f"Report file not found: {file_path}")
    except Exception as e:
        st.error(f"Error reading report: {str(e)}")


def main():
    """Main Streamlit application."""
    
    # Header
    st.markdown('<h1 class="main-header">📊 Investment Report Generator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">AI-powered investment analysis with Upsonic Agent Framework</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("🔧 Configuration")
        
        # API Status
        api_status = check_api_health()
        if api_status:
            st.success("✅ API is running")
        else:
            st.error("❌ API is not available")
            st.info("Please start the FastAPI backend:\n```bash\nuv run uvicorn src.api.main:app --reload\n```")
            return
        
        st.header("📋 Example Companies")
        
        examples = {
            "Tech Giants": "AAPL, MSFT, GOOGL",
            "Semiconductors": "NVDA, AMD, INTC", 
            "Automotive": "TSLA, F, GM",
            "Banking": "JPM, BAC, GS",
            "Retail": "AMZN, WMT, TGT",
            "Healthcare": "PFE, JNJ, MRNA",
            "Energy": "XOM, CVX, BP"
        }
        
        for category, symbols in examples.items():
            with st.expander(f"🏢 {category}"):
                st.code(symbols)
                if st.button(f"Use {category}", key=f"use_{category}"):
                    st.session_state.companies = symbols
                    st.rerun()
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="analysis-card">', unsafe_allow_html=True)
        st.header("🚀 Start Analysis")
        
        # Input form
        with st.form("analysis_form"):
            companies = st.text_input(
                "Company Symbols (comma-separated)",
                value=st.session_state.get("companies", ""),
                placeholder="e.g., AAPL, MSFT, GOOGL",
                help="Enter stock symbols separated by commas"
            )
            
            message = st.text_area(
                "Analysis Instructions",
                value=st.session_state.get("message", ""),
                placeholder="Generate comprehensive investment analysis and portfolio allocation recommendations",
                height=100,
                help="Customize the analysis instructions"
            )
            
            submitted = st.form_submit_button("🔍 Generate Analysis", type="primary")
            
            if submitted:
                if not companies.strip():
                    st.error("Please enter at least one company symbol")
                else:
                    with st.spinner("Starting analysis..."):
                        analysis_id = start_analysis(companies.strip(), message.strip())
                        
                        if analysis_id:
                            st.session_state.current_analysis = analysis_id
                            st.success(f"Analysis started! ID: {analysis_id}")
                            st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.header("💡 Tips")
        
        st.markdown("""
        <div class="company-example">
        <strong>📈 How to use:</strong><br>
        1. Enter company symbols (e.g., AAPL, MSFT)<br>
        2. Customize analysis instructions<br>
        3. Click "Generate Analysis"<br>
        4. Wait for results and download reports
        </div>
        """, unsafe_allow_html=True)
        
        st.info("💡 **Tip**: Use the example companies from the sidebar for quick testing!")
    
    # Analysis Results
    if "current_analysis" in st.session_state:
        st.header("📊 Analysis Results")
        
        analysis_id = st.session_state.current_analysis
        
        # Progress tracking
        with st.container():
            result = get_analysis_result(analysis_id)
            
            if result:
                status = result.get("status", "unknown")
                
                if status == "running":
                    st.markdown(f'<div class="status-box status-running">🔄 Analysis in progress... (ID: {analysis_id})</div>', unsafe_allow_html=True)
                    
                    # Auto-refresh every 5 seconds
                    time.sleep(2)
                    st.rerun()
                    
                elif status == "completed":
                    st.markdown(f'<div class="status-box status-completed">✅ Analysis completed! (ID: {analysis_id})</div>', unsafe_allow_html=True)
                    
                    # Display summary
                    if "summary" in result:
                        st.subheader("📋 Summary")
                        st.text(result["summary"])
                    
                    # Display reports
                    if "reports" in result and result["reports"]:
                        st.subheader("📄 Generated Reports")
                        
                        reports = result["reports"]
                        
                        # Create tabs for different reports
                        tab1, tab2, tab3 = st.tabs(["📊 Stock Analysis", "🏆 Investment Ranking", "💼 Portfolio Strategy"])
                        
                        with tab1:
                            if "stock_analysis" in reports:
                                display_report_content(reports["stock_analysis"])
                        
                        with tab2:
                            if "research_analysis" in reports:
                                display_report_content(reports["research_analysis"])
                        
                        with tab3:
                            if "portfolio_strategy" in reports:
                                display_report_content(reports["portfolio_strategy"])
                        
                        # Download buttons
                        st.subheader("⬇️ Download Reports")
                        
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            if "stock_analysis" in reports:
                                try:
                                    with open(reports["stock_analysis"], 'r', encoding='utf-8') as f:
                                        st.download_button(
                                            "📊 Stock Analysis",
                                            f.read(),
                                            file_name=f"stock_analysis_{analysis_id[:8]}.md",
                                            mime="text/markdown"
                                        )
                                except:
                                    st.error("Could not load stock analysis report")
                        
                        with col2:
                            if "research_analysis" in reports:
                                try:
                                    with open(reports["research_analysis"], 'r', encoding='utf-8') as f:
                                        st.download_button(
                                            "🏆 Investment Ranking",
                                            f.read(),
                                            file_name=f"investment_ranking_{analysis_id[:8]}.md",
                                            mime="text/markdown"
                                        )
                                except:
                                    st.error("Could not load research analysis report")
                        
                        with col3:
                            if "portfolio_strategy" in reports:
                                try:
                                    with open(reports["portfolio_strategy"], 'r', encoding='utf-8') as f:
                                        st.download_button(
                                            "💼 Portfolio Strategy",
                                            f.read(),
                                            file_name=f"portfolio_strategy_{analysis_id[:8]}.md",
                                            mime="text/markdown"
                                        )
                                except:
                                    st.error("Could not load portfolio strategy report")
                
                elif status == "failed":
                    st.markdown(f'<div class="status-box status-failed">❌ Analysis failed (ID: {analysis_id})</div>', unsafe_allow_html=True)
                    
                    if "error" in result:
                        st.error(f"Error: {result['error']}")
                
                else:
                    st.warning(f"Unknown status: {status}")
            
            else:
                st.error("Could not retrieve analysis results")
        
        # Clear analysis button
        if st.button("🗑️ Clear Results"):
            if "current_analysis" in st.session_state:
                del st.session_state.current_analysis
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div class="footer">
        <p>⚠️ <strong>Disclaimer:</strong> This tool is for educational and research purposes only. 
        It should not be considered as financial advice. Always consult with qualified financial advisors 
        before making investment decisions.</p>
        <p>Built with ❤️ using Upsonic Agent Framework, FastAPI, and Streamlit</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
