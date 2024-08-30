import jwt
from datetime import timedelta, datetime
import os
import time


def create_jwt(id, exprires_in = timedelta(hours=1)):
    payload = {
        "id": id,
        "exp": (datetime.now() + exprires_in).timestamp()  # Token expiration time
    }
    JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")
    return token


def decode_jwt(token):
    try:
        JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        print("Token has expired")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token")
        return None