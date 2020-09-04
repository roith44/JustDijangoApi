from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers

class HelloApiView(APIView):
    """text api view"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format = None):
        """Return a list of APIView feature"""
        an_apiview = [
            'use HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Give you the most control over you application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello','an_apiview': an_apiview})

    def post(self, request):
        """create a hello massage with our name"""
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            massage = f'hello {name}'
            return Response({'massage': massage})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk = None):
        """handle updatin on object"""
        return Response({'method': 'Put'})
    def patch(self, request, pk = None):
        """handle partial upadate an object"""
        return Response({'method': 'Patch'})

    def delete(self, request, pk = None):
        """Delete an object"""
        return Response({'mehtod': 'Delete'})


        