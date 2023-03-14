"""View module for handling requests about venues"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from backendapi.models import Venue


class VenueView(ViewSet):
    """36one5 venues view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single venue

        Returns:
            Response -- JSON serialized venue
        """
        try:
            venue = Venue.objects.get(pk=pk)
        except Venue.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        serialized = VenueSerializer(venue)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests to get all venues

        Returns:
            Response -- JSON serialized list of venues
        """
        venues = Venue.objects.all()
        serializer = VenueSerializer(venues, many=True)
        return Response(serializer.data)
    
class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for user
    """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'date_joined', 'is_staff')

class VenueSerializer(serializers.ModelSerializer):
    """JSON serializer for venues
    """
    admin_user = UserSerializer(many=False)

    class Meta:
        model = Venue
        fields = ('id', 'name', 'location', 'admin_user', 'hours', 'details', 'coordinates', 'website', 'venue_image')
