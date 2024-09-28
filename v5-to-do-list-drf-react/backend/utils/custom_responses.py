from rest_framework.response import Response
from datetime import datetime
from humps import camelize
from http import HTTPStatus


def _get_base_response(status:int, **kwargs) -> Response:
    return Response(camelize(**kwargs), status=status)


def get_success_response(status:int, **kwargs) -> Response:
    return _get_base_response(
        status=status, 
        **kwargs
    )


def get_error_response(status:int, message:str="", **kwargs) -> Response:
    return _get_base_response(
        message=message or HTTPStatus(status).phrase,  # If a message is not provided, one is obtained by default
        timestamp=datetime.now().isoformat(),
        status=status,
        **kwargs
    )
