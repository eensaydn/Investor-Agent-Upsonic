"""Start both API and Streamlit servers."""

import subprocess
import sys
import time
import threading
from src.config.settings import settings

def run_api():
    """Run FastAPI server."""
    print("Starting FastAPI backend...")
    subprocess.run([sys.executable, "run_api.py"])

def run_streamlit():
    """Run Streamlit frontend."""
    print("Starting Streamlit frontend...")
    time.sleep(3)  # Wait for API to start
    subprocess.run([sys.executable, "run_streamlit.py"])

if __name__ == "__main__":
    print(f"Starting {settings.APP_NAME}")
    print("=" * 50)
    print("This will start both:")
    print("  - FastAPI Backend (port 8001)")
    print("  - Streamlit Frontend (port 8501)")
    print("=" * 50)
    
    # Start both servers in parallel
    api_thread = threading.Thread(target=run_api)
    streamlit_thread = threading.Thread(target=run_streamlit)
    
    api_thread.start()
    streamlit_thread.start()
    
    try:
        api_thread.join()
        streamlit_thread.join()
    except KeyboardInterrupt:
        print("\nShutting down servers...")
        sys.exit(0)
