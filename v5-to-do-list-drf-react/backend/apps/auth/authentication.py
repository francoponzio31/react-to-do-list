from rest_framework.authentication import BaseAuthentication
from utils.custom_exceptions import AuthenticationFailedException
from apps.users.models import User
from .utils import decode_token


class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        payload = decode_token(request)

        try:
            user = User.objects.get(id=payload["user_id"])
        except User.DoesNotExist:
            return AuthenticationFailedException

        return (user, None)
