from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from services.video_service import VideoService

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/', methods=['GET'])
@jwt_required()
def get_dashboard():
    videos = VideoService.select_dashboard_videos()
    return jsonify({'videos': videos}), 200
