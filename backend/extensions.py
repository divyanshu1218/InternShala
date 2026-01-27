from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# We will use raw pymongo MongoClient for better control or flask_pymongo
# Using PyMongo from flask_pymongo is standard but pymongo directly is also fine.
# Let's use logic to support a global db instance.

mongo_client = None
jwt = JWTManager()
cors = CORS()

def init_extensions(app):
    global mongo_client
    # Initialize MongoDB Client
    try:
        mongo_client = MongoClient(app.config['MONGO_URI'])
        # Quick check
        mongo_client.admin.command('ping')
        print("Connected to MongoDB successfully.")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
    
    # Initialize JWT
    jwt.init_app(app)
    
    # Initialize CORS
    cors.init_app(app, resources={r"/*": {"origins": "*"}})

def get_db():
    if mongo_client:
        # Default database from URI or named explicitly
        return mongo_client.get_database()
    return None
