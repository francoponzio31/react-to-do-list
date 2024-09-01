from rest_framework.response import Response


def get_response_message(success:bool, message:str, status:int=200, **kwargs) -> Response:
    response_data = {
        "success": success,
        "message": message,
        **kwargs
    }
    return Response(response_data, status=status)