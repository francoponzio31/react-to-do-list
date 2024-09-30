from rest_framework.renderers import JSONRenderer
from rest_framework import parsers
import humps


class SnakeCaseParser(parsers.JSONParser):
    def parse(self, stream, media_type=None, parser_context=None):
        data = super().parse(stream, media_type=media_type, parser_context=parser_context)
        return humps.decamelize(data)


class CamelCaseRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, dict):
            data = humps.camelize(data)
        return super().render(data, accepted_media_type, renderer_context)


class DecamelizeQueryParamsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.GET:
            query_params = request.GET.dict()
            decamelized_query = humps.decamelize(query_params)
            request.GET = request.GET.copy()
            request.GET.update(decamelized_query)

        response = self.get_response(request)
        return response
