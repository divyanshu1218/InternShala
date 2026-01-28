from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS

mongo = PyMongo()
jwt = JWTManager()
bcrypt = Bcrypt()
# Allow all origins for development (restrict in production)
cors = CORS(resources={r"/*": {"origins": "*"}})
