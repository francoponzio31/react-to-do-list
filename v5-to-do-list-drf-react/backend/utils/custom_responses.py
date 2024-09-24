from rest_framework.response import Response
from datetime import datetime
from humps import camelize
from http import HTTPStatus
from rest_framework import status


def _get_base_response(status:int, message:str, **kwargs) -> Response:
    response_data = {
        "message": message or HTTPStatus(status).phrase,
        **kwargs
    }
    return Response(camelize(response_data), status=status)


def get_success_response(status:int=status.HTTP_200_OK, message:str="", **kwargs) -> Response:
    return _get_base_response(message=message, status=status, **kwargs)


def get_error_response(status:int=status.HTTP_500_INTERNAL_SERVER_ERROR, message:str="", **kwargs) -> Response:
    return _get_base_response(message=message, status=status, timestamp=datetime.now().isoformat(), **kwargs)
