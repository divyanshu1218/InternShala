from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    
    user, error = AuthService.register_user(name, email, password)
    if error:
        return jsonify({'error': error}), 400
        
    return jsonify({'message': 'User registered successfully', 'user': user}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    token, error = AuthService.authenticate_user(email, password)
    if error:
        return jsonify({'error': error}), 401
        
    return jsonify({'access_token': token}), 200

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    current_user_id = get_jwt_identity()
    user, error = AuthService.get_user_profile(current_user_id)
    
    if error:
        return jsonify({'error': error}), 404
        
    return jsonify(user), 200

@auth_bp.route('/logout', methods=['POST'])
# @jwt_required() - Optional: Require login to logout?
# For stateless JWT, logout is usually client-side removal of token.
# We can just return success here.
def logout():
    return jsonify({'message': 'Logout successful'}), 200
