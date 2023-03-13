"""View module for handling requests about profiles"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from backendapi.models import Profile


class ProfileView(ViewSet):
    """36one5 profiles view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single profile

        Returns:
            Response -- JSON serializer profile
        """
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests to get all profiles

        Returns:
            Response -- JSON serializer list of profiles
        """
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for user
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined', 'is_staff')

class ProfileSerializer(serializers.ModelSerializer):
    """JSON serializer for profiles
    """

    user = UserSerializer(many=False)

    class Meta:
        model = Profile
        fields = ('id', 'full_name', 'user', 'bio', )
