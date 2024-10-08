from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings




from profiles_api import models
from profiles_api import serializers
from profiles_api import permission


class HelloApiview(APIView):
    """Test API View"""

    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview =[
            'Uses HTTP methods as function(get, post, patch, put,delete)',
            'Is similar to a traditional Django Views',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs'

        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, 
                            status = status.HTTP_400_BAD_REQUEST
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
    
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
               serializer.errors,
               status=status.HTTP_400_BAD_REQUEST 
            )
    def retrieve(self, requestr, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle updating part of the object"""
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """Handle removung an object"""
        return Response({'http_method': 'DELETE'})
    

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authenticatio_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fiels = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle obtaing user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



        

    
                         

