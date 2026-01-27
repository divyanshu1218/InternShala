from flask_jwt_extended import create_access_token
from backend.models.user import User

class AuthService:
    @staticmethod
    def register_user(name, email, password):
        """
        Registers a new user.
        Returns: Tuple (user_dict, error_message)
        """
        if not name or not email or not password:
            return None, "Missing fields"
        
        user = User.create_user(name, email, password)
        if not user:
            return None, "Email already registered"
            
        return user.to_dict(), None

    @staticmethod
    def authenticate_user(email, password):
        """
        Authenticates a user.
        Returns: Tuple (access_token, error_message)
        """
        user = User.find_by_email(email)
        if not user or not user.verify_password(password):
            return None, "Invalid email or password"
            
        access_token = create_access_token(identity=str(user._id))
        return access_token, None

    @staticmethod
    def get_user_profile(user_id):
        """
        Gets a user's profile.
        Returns: Tuple (user_dict, error_message)
        """
        user = User.find_by_id(user_id)
        if not user:
            return None, "User not found"
            
        return user.to_dict(), None
