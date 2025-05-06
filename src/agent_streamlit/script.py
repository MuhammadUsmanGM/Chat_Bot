import os
import sys
from streamlit.web import cli

def app():
    sys.argv = ("streamlit","run","src/agent_streamlit/main.py")
    cli.main()

if __name__ == "__main__":
    app()