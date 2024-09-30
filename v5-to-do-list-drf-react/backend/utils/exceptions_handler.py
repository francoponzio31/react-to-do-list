from rest_framework.views import exception_handler
from utils.custom_responses import get_error_response
from utils.custom_exceptions import AuthenticationFailedException
from rest_framework import status
import logging


logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):

    logger.error("--- UNHANDLED ERROR ---")
    logger.exception(exc)
    
    response = exception_handler(exc, context)

    if response is None:
        response = get_error_response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, message="An unexpected error occurred")

    if isinstance(exc, AuthenticationFailedException):
        response = get_error_response(status=status.HTTP_401_UNAUTHORIZED, message="Error decoding Auth token")

    return response