from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from backend.services.video_service import VideoService

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/', methods=['GET'])
@jwt_required()
def get_dashboard():
    """
    Returns exactly 2 active videos with playback tokens.
    Backend decides which videos to show.
    """
    videos = VideoService.select_dashboard_videos()
    return jsonify({'videos': videos}), 200
