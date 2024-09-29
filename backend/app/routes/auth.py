from flask import request, jsonify
from services.auth_service import AuthService
from routes import auth

@auth.route('/signup', methods=['POST'])
def signup():
    data = request.json
    user = AuthService.signup(data)
    return jsonify({'success': True, 'user': user}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    token = AuthService.login(data)
    return jsonify({'success': True, 'token': token}), 200


