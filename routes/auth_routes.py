from flask import Blueprint, request, jsonify
from services.auth_service import register_user, login_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    return jsonify(register_user(request.json))

@auth_bp.route('/login', methods=['POST'])
def login():
    return jsonify(login_user(request.json))