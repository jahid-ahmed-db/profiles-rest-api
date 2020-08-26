from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from profiles_api import serializer


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializer.HelloSerializer



    def get(self, request, format=None):
        """Returns a list of APIviews features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',   
            'Is similar to a traditional Django View',
            'Gives you most control over your application logic',
            'Is mapped manually to URLs',
            'Welcome to our API'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview })

    def post(self, request): # request is example of handler which will hold client post request data
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data) # this invoke the class "Hello serializer" in serializer.py

        if serializer.is_valid(): #validate client post request data meet serializer max_length
            name  = serializer.validated_data.get('name') # get () is a method that returns the value of the item with the specified key.
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )

  
    def put(self, request, pk=None):
        """Handle updating an object"""
    
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """Handle partial update of object"""
    
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete an object"""
    
        return Response({'method': 'DELETE'})