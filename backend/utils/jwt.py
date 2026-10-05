import os
from datetime import datetime, timedelta, timezone

import jwt
from dotenv import load_dotenv


load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_MINUTES = 30

def create_access_token(customer_id):

    expiration = datetime.now(timezone.utc) + timedelta(
        minutes=JWT_EXPIRATION_MINUTES
    )

    payload = {
        "sub": str(customer_id),
        "exp": expiration
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM
    )

def decode_access_token(token):

    try:
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )

        return payload

    except jwt.ExpiredSignatureError:
        return None

    except jwt.InvalidTokenError:
        return None