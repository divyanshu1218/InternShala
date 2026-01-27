from datetime import datetime
from bson import ObjectId
from backend.extensions import get_db
from backend.utils.security import hash_password, verify_password

class User:
    collection_name = 'users'

    def __init__(self, name, email, password_hash, _id=None, created_at=None):
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self._id = _id
        self.created_at = created_at or datetime.utcnow()

    @classmethod
    def create_user(cls, name, email, password):
        """Creates a new user with hashed password."""
        db = get_db()
        if db.users.find_one({'email': email}):
            return None  # User already exists

        hashed = hash_password(password)
        user_doc = {
            'name': name,
            'email': email,
            'password_hash': hashed,
            'created_at': datetime.utcnow()
        }
        
        result = db.users.insert_one(user_doc)
        return cls(name=name, email=email, password_hash=hashed, _id=result.inserted_id, created_at=user_doc['created_at'])

    @classmethod
    def find_by_email(cls, email):
        """Finds a user by email."""
        db = get_db()
        user_doc = db.users.find_one({'email': email})
        if not user_doc:
            return None
        return cls(**user_doc)

    @classmethod
    def find_by_id(cls, user_id):
        """Finds a user by ID."""
        db = get_db()
        try:
            oid = ObjectId(user_id)
        except:
            return None
        user_doc = db.users.find_one({'_id': oid})
        if not user_doc:
            return None
        return cls(**user_doc)

    def verify_password(self, password):
        """Check password against hash."""
        return verify_password(password, self.password_hash)

    def to_dict(self):
        """Return public user data."""
        return {
            'id': str(self._id),
            'name': self.name,
            'email': self.email
        }
