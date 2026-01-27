from backend.extensions import mongo
from bson import ObjectId

class Video:
    def __init__(self, data):
        self._id = data.get('_id')
        self.title = data.get('title')
        self.description = data.get('description')
        self.youtube_id = data.get('youtube_id')
        self.thumbnail_url = data.get('thumbnail_url')
        self.is_active = data.get('is_active')

    @staticmethod
    def get_active_videos(limit=2):
        # In a real app, logic might be more complex (randomize etc)
        # Here we just take 2 active videos
        cursor = mongo.db.videos.find({"is_active": True}).limit(limit)
        return [Video(doc) for doc in cursor]

    @staticmethod
    def find_by_id(video_id):
        try:
            data = mongo.db.videos.find_one({"_id": ObjectId(video_id)})
            if data:
                return Video(data)
        except:
            pass
        return None

    def to_dict(self):
        return {
            "id": str(self._id),
            "title": self.title,
            "description": self.description,
            "thumbnail_url": self.thumbnail_url,
            # Playback token is added by service, not model
        }
