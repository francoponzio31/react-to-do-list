from rest_framework.response import Response
from datetime import datetime
from humps import camelize


def _get_base_response(success:bool, message:str, status:int, **kwargs) -> Response:
    response_data = {
        "success": success,
        "message": message,
        **kwargs
    }
    return Response(camelize(response_data), status=status)


def get_success_response(message:str, status:int=200, **kwargs) -> Response:
    return _get_base_response(success=True, message=message, status=status, **kwargs)


def get_error_response(message:str, status:int=500, **kwargs) -> Response:
    return _get_base_response(success=False, message=message, status=status, timestamp=datetime.now().isoformat(), **kwargs)
