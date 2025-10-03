"""Run the Streamlit frontend application."""

import subprocess
import sys
from src.config.settings import settings

if __name__ == "__main__":
    print(f"Starting {settings.APP_NAME} Streamlit Frontend")
    print(f"Port: {settings.STREAMLIT_PORT}")
    print("Frontend URL: http://localhost:8501")
    
    # Run Streamlit
    subprocess.run([
        sys.executable, "-m", "streamlit", "run", 
        "src/frontend/app.py",
        "--server.port", str(settings.STREAMLIT_PORT),
        "--server.address", "localhost"
    ])
