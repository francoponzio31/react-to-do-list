from apps.users.models import User
from .utils import hash_password, check_hashed_password, encode_token
from utils.custom_exceptions import InvalidCredentialsError, UsernameAlreadyRegisteredError


def login(username: str, password: str) -> User:
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise InvalidCredentialsError
    
    if not check_hashed_password(password, user.password):
        raise InvalidCredentialsError
    
    return encode_token(user.id, username), user


def signup(username: str, password: str) -> User:
    if User.objects.filter(username=username).exists():
        raise UsernameAlreadyRegisteredError
    
    user = User(username=username)
    user.password = hash_password(password)
    user.save()

    return user
