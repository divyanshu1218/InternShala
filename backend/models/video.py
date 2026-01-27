from bson import ObjectId
from backend.extensions import get_db

class Video:
    collection_name = 'videos'

    def __init__(self, title, description, youtube_id, thumbnail_url, is_active=True, _id=None):
        self.title = title
        self.description = description
        self.youtube_id = youtube_id
        self.thumbnail_url = thumbnail_url
        self.is_active = is_active
        self._id = _id

    @classmethod
    def get_active_videos(cls, limit=2):
        """Fetch active videos."""
        db = get_db()
        # Find active videos, maybe randomized or tailored later. 
        # For now, just find active ones.
        videos_cursor = db.videos.find({'is_active': True}).limit(limit)
        return [cls(**doc) for doc in videos_cursor]

    @classmethod
    def find_by_id(cls, video_id):
        """Finds a video by ID."""
        db = get_db()
        try:
            oid = ObjectId(video_id)
        except:
            return None
        video_doc = db.videos.find_one({'_id': oid})
        if not video_doc:
            return None
        return cls(**video_doc)

    def to_dict(self):
        """
        Return public video data.
        CRITICAL: Never expose youtube_id here.
        """
        return {
            'id': str(self._id),
            'title': self.title,
            'description': self.description,
            'thumbnail_url': self.thumbnail_url
        }
