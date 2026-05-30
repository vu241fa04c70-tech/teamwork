from models.user_model import User
from config.database import db
import jwt
import datetime

SECRET_KEY = "secretkey"

def register_user(data):

    user = User(
        username=data['username'],
        email=data['email'],
        password=data['password']
    )

    db.session.add(user)
    db.session.commit()

    return {"message":"User Registered"}

def login_user(data):

    user = User.query.filter_by(email=data['email']).first()

    if user and user.password == data['password']:

        token = jwt.encode({
            'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY)

        return {"token":token}

    return {"message":"Invalid Credentials"}