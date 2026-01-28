import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app

app = create_app()

# This is required for Vercel
if __name__ == "__main__":
    app.run()
