import jwt
import datetime
from flask import current_app

def create_playback_token(video_id):
    """
    Generates a short-lived signed token for video playback.
    This is NOT the user authentication token.
    """
    payload = {
        'video_id': str(video_id),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config['PLAYBACK_TOKEN_EXPIRES_MINUTES']),
        'iat': datetime.datetime.utcnow()
    }
    
    token = jwt.encode(
        payload,
        current_app.config['PLAYBACK_TOKEN_SECRET'],
        algorithm='HS256'
    )
    return token

def decode_playback_token(token):
    """
    Decodes and validates the playback token.
    Returns the payload if valid, None otherwise.
    """
    try:
        payload = jwt.decode(
            token,
            current_app.config['PLAYBACK_TOKEN_SECRET'],
            algorithms=['HS256']
        )
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
