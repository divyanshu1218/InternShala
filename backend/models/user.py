from extensions import mongo, bcrypt
from datetime import datetime
from bson import ObjectId

class User:
    def __init__(self, data):
        self._id = data.get('_id')
        self.name = data.get('name')
        self.email = data.get('email')
        self.password_hash = data.get('password_hash')
        self.created_at = data.get('created_at')

    @staticmethod
    def create_user(name, email, password):
        if User.find_by_email(email):
            return None
        
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
        user_data = {
            "name": name,
            "email": email,
            "password_hash": password_hash,
            "created_at": datetime.utcnow()
        }
        
        result = mongo.db.users.insert_one(user_data)
        user_data['_id'] = result.inserted_id
        return User(user_data)

    @staticmethod
    def find_by_email(email):
        user_data = mongo.db.users.find_one({"email": email})
        if user_data:
            return User(user_data)
        return None

    @staticmethod
    def find_by_id(user_id):
        try:
            user_data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
            if user_data:
                return User(user_data)
        except:
            pass
        return None

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": str(self._id),
            "name": self.name,
            "email": self.email
        }
