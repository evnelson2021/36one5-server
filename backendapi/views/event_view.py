"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from backendapi.models import Event, Venue, EventType


class EventView(ViewSet):
    """36one5 events view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event

        Returns:
            Response -- JSON serializer event
        """
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests to get all events

        Returns:
            Response -- JSON serializer list of events
        """
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EventVenueSerializer(serializers.ModelSerializer):
    """JSON serializer for user
    """
    class Meta:
        model = Venue
        fields = ('id', 'name', 'location', 'admin_user')

class EventTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for user
    """
    class Meta:
        model = EventType
        fields = ('id', 'label')

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    venue = EventVenueSerializer(many=False)
    event_type = EventTypeSerializer(many=False)

    class Meta:
        model = Event
        fields = ('id', 'name', 'venue', 'date', 'doors', 'start_time', 'event_type', 'details', 'ticket_link')
