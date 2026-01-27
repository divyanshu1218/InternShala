from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    user, error = AuthService.register_user(data.get('name'), data.get('email'), data.get('password'))
    
    if error:
        return jsonify({'error': error}), 400
        
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    token, error = AuthService.authenticate_user(data.get('email'), data.get('password'))
    
    if error:
        return jsonify({'error': error}), 401
        
    return jsonify({'token': token}), 200

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user, error = AuthService.get_user_profile(user_id)
    
    if error:
        return jsonify({'error': error}), 404
        
    return jsonify(user), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    # In a stateless JWT setup, client just discards token.
    # We could implement a blocklist here if strict logout needed.
    return jsonify({'message': 'Logged out successfully'}), 200
