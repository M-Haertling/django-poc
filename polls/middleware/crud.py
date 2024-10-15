
from django.http import HttpRequest
from django.http import HttpResponse
from django.urls import ResolverMatch
from polls.registry import crudRegistry
from rest_framework.response import Response

class CRUDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('INIT Middleware')

    def __call__(self, request: HttpRequest):
        print('test1')
        for path, view in crudRegistry._registry:
            print('patterns', path.url_patterns)
            print('app_name', path.app_name)
            print('pattern', path.pattern)
            response: Response = path.resolve(request.path).func(request)
            return response.render()
        
        response = self.get_response(request)
        return response