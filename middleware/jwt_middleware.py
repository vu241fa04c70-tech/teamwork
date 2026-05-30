import jwt
from functools import wraps
from flask import request, jsonify

SECRET_KEY = "secretkey"

def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"message":"Token Missing"}),401

        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except:
            return jsonify({"message":"Invalid Token"}),401

        return f(*args, **kwargs)

    return decorated