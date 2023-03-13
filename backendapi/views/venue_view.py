"""View module for handling requests about venues"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from backendapi.models import Venue


class VenueView(ViewSet):
    """36one5 venues view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single venue

        Returns:
            Response -- JSON serialized venue
        """
        venue = Venue.objects.get(pk=pk)
        serializer = VenueSerializer(venue)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all venues

        Returns:
            Response -- JSON serialized list of venues
        """
        venues = Venue.objects.all()
        serializer = VenueSerializer(venues, many=True)
        return Response(serializer.data)

class VenueSerializer(serializers.ModelSerializer):
    """JSON serializer for venues
    """
    class Meta:
        model = Venue
        fields = ('id', 'admin_user', 'name', 'location', 'hours', 'details', 'coordinates')
