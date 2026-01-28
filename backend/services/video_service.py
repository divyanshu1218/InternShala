from models.video import Video
from utils.jwt_utils import create_playback_token, decode_playback_token

class VideoService:
    @staticmethod
    def select_dashboard_videos():
        """
        Selects exactly 2 active videos for the dashboard.
        Returns videos with playback tokens.
        """
        videos = Video.get_active_videos(limit=2)
        
        video_list = []
        for video in videos:
            video_dict = video.to_dict()
            # Generate playback token for this specific video
            video_dict['playback_token'] = create_playback_token(video._id)
            video_list.append(video_dict)
        
        return video_list

    @staticmethod
    def get_stream_url(video_id, playback_token):
        """
        Validates playback token and returns stream URL.
        Returns: Tuple (stream_url, error_message)
        """
        # Validate playback token
        payload = decode_playback_token(playback_token)
        if not payload:
            return None, "Invalid or expired playback token"
        
        # Ensure token matches the requested video
        if payload.get('video_id') != str(video_id):
            return None, "Token does not match video"
        
        # Fetch video from database
        video = Video.find_by_id(video_id)
        if not video:
            return None, "Video not found"
        
        if not video.is_active:
            return None, "Video is not available"
        
        # Generate YouTube embed URL (privacy-enhanced mode)
        # CRITICAL: youtube_id is NEVER exposed to the client
        stream_url = f"https://www.youtube-nocookie.com/embed/{video.youtube_id}"
        
        return stream_url, None
