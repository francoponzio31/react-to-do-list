import bcrypt
import jwt
from rest_framework.authentication import get_authorization_header
from django.conf import settings
import logging
from utils.custom_exceptions import AuthenticationFailedException
import datetime


def hash_password(raw_password:str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(raw_password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")


def check_hashed_password(raw_password:str, hashed_password:str) -> bool:
    return bcrypt.checkpw(raw_password.encode("utf-8"), hashed_password.encode("utf-8"))


def decode_token(request) -> dict:
    auth_header = get_authorization_header(request).decode("utf-8")
    token = None
    try:
        token = auth_header.split("Bearer ")[1]
    except IndexError:
        logging.warning("Incorrect token format")
        raise AuthenticationFailedException

    if not token:
        logging.warning("Incorrect token format")
        return AuthenticationFailedException

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY_JWT,
            algorithms=[settings.JWT_ALGORITHM],
            options={"verify_exp": settings.JWT_VERIFY_EXPIRATION},
        )

        required_fields = {"user_id", "username"}
        if not required_fields.issubset(set(payload.keys())):
            logging.warning("Token payload required fields left")
            raise AuthenticationFailedException

        return payload

    except jwt.ExpiredSignatureError:
        logging.warning("JWT decoding error: Signature has expired.")
    except jwt.DecodeError:
        logging.warning("JWT decoding error: Error decoding signature.")
    except jwt.InvalidTokenError:
        logging.warning("JWT decoding error: Invalid token.")
    except Exception as e:
        logging.warning(f"JWT decoding error: {str(e)}")

    raise AuthenticationFailedException


def encode_token(user_id:int, username:str) -> str:

    payload = {
        "user_id": user_id,
        "username": username,
        "iat": datetime.datetime.now(),
        "exp": datetime.datetime.now() + datetime.timedelta(hours=8),  # Token valid for 8 hours
    }

    token = jwt.encode(payload, settings.SECRET_KEY_JWT, settings.JWT_ALGORITHM)

    return token
