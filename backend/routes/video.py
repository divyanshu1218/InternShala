from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from backend.services.video_service import VideoService

video_bp = Blueprint('video', __name__)

@video_bp.route('/<video_id>/stream', methods=['GET'])
@jwt_required()
def get_stream(video_id):
    """
    Returns the stream URL for a video.
    Requires valid JWT and playback token.
    """
    playback_token = request.args.get('token')
    
    if not playback_token:
        return jsonify({'error': 'Playback token required'}), 400
    
    stream_url, error = VideoService.get_stream_url(video_id, playback_token)
    
    if error:
        return jsonify({'error': error}), 403
    
    return jsonify({'stream_url': stream_url}), 200
