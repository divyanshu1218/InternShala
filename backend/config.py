import os
import secrets
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(32)
    
    # MongoDB Config
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/videostreamapp'
    
    # JWT Config
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or secrets.token_hex(32)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES_MINUTES', 30)))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    
    # Video Security
    PLAYBACK_TOKEN_SECRET = os.environ.get('PLAYBACK_TOKEN_SECRET') or secrets.token_hex(32)
    PLAYBACK_TOKEN_EXPIRES_MINUTES = int(os.environ.get('PLAYBACK_TOKEN_EXPIRES_MINUTES', 5))
    
    # CORS
    CORS_HEADERS = 'Content-Type'
