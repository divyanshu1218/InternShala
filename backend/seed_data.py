"""
Database seeding script for video streaming app.
Run this script to populate the database with initial video data.
"""
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB connection
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/videostreamapp')

def seed_database():
    try:
        client = MongoClient(MONGO_URI)
        db = client.get_database()
        
        print("Connected to MongoDB successfully.")
        
        # Clear existing data (optional - comment out if you want to keep existing data)
        # db.videos.delete_many({})
        # db.users.delete_many({})
        # print("Cleared existing data.")
        
        # Sample videos - Replace with actual YouTube video IDs
        videos = [
            {
                'title': 'Introduction to Python Programming',
                'description': 'Learn the basics of Python programming',
                'youtube_id': 'kqtD5dpn9C8',  # Replace with actual YouTube ID
                'thumbnail_url': 'https://img.youtube.com/vi/kqtD5dpn9C8/maxresdefault.jpg',
                'is_active': True
            },
            {
                'title': 'Web Development Crash Course',
                'description': 'Complete web development tutorial for beginners',
                'youtube_id': 'UB1O30fR-EE',  # Replace with actual YouTube ID
                'thumbnail_url': 'https://img.youtube.com/vi/UB1O30fR-EE/maxresdefault.jpg',
                'is_active': True
            },
            {
                'title': 'Machine Learning Fundamentals',
                'description': 'Introduction to machine learning concepts',
                'youtube_id': 'ukzFI9rgwfU',  # Replace with actual YouTube ID
                'thumbnail_url': 'https://img.youtube.com/vi/ukzFI9rgwfU/maxresdefault.jpg',
                'is_active': True
            }
        ]
        
        # Insert videos
        if db.videos.count_documents({}) == 0:
            result = db.videos.insert_many(videos)
            print(f"Inserted {len(result.inserted_ids)} videos.")
        else:
            print("Videos already exist. Skipping video insertion.")
        
        # Create indexes
        db.users.create_index('email', unique=True)
        db.videos.create_index('is_active')
        print("Created indexes.")
        
        print("\n✅ Database seeded successfully!")
        print(f"Total videos: {db.videos.count_documents({})}")
        print(f"Total users: {db.users.count_documents({})}")
        
        client.close()
        
    except Exception as e:
        print(f"❌ Error seeding database: {e}")

if __name__ == '__main__':
    seed_database()
