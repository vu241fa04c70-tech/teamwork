from flask import Blueprint, request, jsonify
from services.auth_service import register_user, login_user

auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Register User
    ---
    tags:
      - Authentication

    consumes:
      - application/json

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              example: Kanchana
            email:
              type: string
              example: kanchana@gmail.com
            password:
              type: string
              example: 1234

    responses:
      200:
        description: User Registered Successfully
    """
    return jsonify(register_user(request.json))
@auth_bp.route('/login', methods=['POST'])
def login():
    """
    User Login
    ---
    tags:
      - Authentication

    consumes:
      - application/json

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              example: kanchana@gmail.com
            password:
              type: string
              example: 1234

    responses:
      200:
        description: Login Successful
        schema:
          type: object
          properties:
            token:
              type: string
    """
    return jsonify(login_user(request.json))