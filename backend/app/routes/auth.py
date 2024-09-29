from flask import request, jsonify
from services.auth_service import AuthService
from routes import auth_bp

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    user = AuthService.signup(data)
    return jsonify({'success': True, 'user': user}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    token = AuthService.login(data)
    if token:
        return jsonify({'success': True, 'token': token}), 200
    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

