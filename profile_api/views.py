from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """text api view"""
    def get(self, request, format = None):
        """Return a list of APIView feature"""
        an_apiview = [
            'use HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Give you the most control over you application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello','an_apiview': an_apiview})
        