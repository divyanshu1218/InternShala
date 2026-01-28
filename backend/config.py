import os
from datetime import timedelta
from dotenv import load_dotenv

# Explicitly load .env from the current directory (backend)
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/videodb')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret-key-change-in-production')
    # ...
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    PLAYBACK_TOKEN_SECRET = os.getenv('PLAYBACK_TOKEN_SECRET', 'video-playback-secret-key')
    PLAYBACK_TOKEN_EXPIRES_MINUTES = 5
