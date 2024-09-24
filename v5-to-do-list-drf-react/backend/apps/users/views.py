from rest_framework.views import APIView
from rest_framework import status
from utils.custom_responses import get_success_response, get_error_response
from .serializers import UserOutputSerializer
from .models import User
from . import services
import logging


logger = logging.getLogger(__name__)

class ListUsersView(APIView):

    def get(self, request):
        try:
            users = services.get_users()
            users_output = UserOutputSerializer(users, many=True)
            return get_success_response(status=status.HTTP_200_OK, users=users_output.data)
        except Exception as ex:
            logger.exception(ex)
            return get_error_response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserDetailView(APIView):
    def get(self, request, user_id):
        try:
            user = services.get_user_by_id(user_id)
            user_output = UserOutputSerializer(user)
            return get_success_response(status=status.HTTP_200_OK, user=user_output.data)
        except User.DoesNotExist as ex:
            logger.error(ex)
            return get_error_response(status=status.HTTP_404_NOT_FOUND, message=f"User with id {user_id} not found")
        except Exception as ex:
            logger.exception(ex)
            return get_error_response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CurrentUserDetailView(APIView):
    def get(self, request):
        try:
            user_output = UserOutputSerializer(request.user)
            return get_success_response(status=status.HTTP_200_OK, user=user_output.data)
        except User.DoesNotExist as ex:
            logger.error(ex)
            return get_error_response(status=status.HTTP_404_NOT_FOUND, message=f"User with id {request.user.id} not found")
        except Exception as ex:
            logger.exception(ex)
            return get_error_response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)