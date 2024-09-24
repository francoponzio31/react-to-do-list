from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from utils.custom_responses import get_success_response, get_error_response
from .serializers import LoginBodySerializer, SignupBodySerializer, UserOutputSerializer
from utils.custom_exceptions import InvalidCredentialsError, UsernameAlreadyRegisteredError
from . import services
import logging


logger = logging.getLogger(__name__)

class LoginView(APIView):

    authentication_classes = []

    def post(self, request):
        try:
            body_serializer = LoginBodySerializer(data=request.data)
            body_serializer.is_valid(raise_exception=True)
            token, user = services.login(**body_serializer.validated_data)
            user_output = UserOutputSerializer(user)
            return get_success_response(status=status.HTTP_200_OK, tokenJWT=token, userDTO=user_output.data)
        except serializers.ValidationError as ex:
            logger.error(ex)
            return get_error_response(status=status.HTTP_400_BAD_REQUEST, message="Invalid user data", errors=body_serializer.errors)
        except InvalidCredentialsError as ex:
            logger.error(ex)
            return get_error_response(status=status.HTTP_401_UNAUTHORIZED, message="Wrong username or password")
        except Exception as ex:
            logger.exception(ex)
            return get_error_response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class SignupView(APIView):

    authentication_classes = []

    def post(self, request):
        try:
            body_serializer = SignupBodySerializer(data=request.data)
            body_serializer.is_valid(raise_exception=True)
            new_user = services.signup(**body_serializer.validated_data)
            user_output = UserOutputSerializer(new_user)
            return get_success_response(status=status.HTTP_201_CREATED, user=user_output.data)
        except serializers.ValidationError as ex:
            logger.error(ex)
            return get_error_response(status=status.HTTP_400_BAD_REQUEST, message="Invalid user data", errors=body_serializer.errors)
        except UsernameAlreadyRegisteredError as ex:
            logger.error(ex)
            return get_error_response(status=status.HTTP_409_CONFLICT, message="A user with this username already exists")
        except Exception as ex:
            logger.exception(ex)
            return get_error_response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

