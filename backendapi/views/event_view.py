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
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized event instance
        """
        venue = Venue.objects.get(pk=request.data["venue"])
        event_type = EventType.objects.get(pk=request.data["event_type"])

        event = Event.objects.create(
            name=request.data["name"],
            date=request.data["date"],
            doors=request.data["doors"],
            start_time=request.data["start_time"],
            details=request.data["details"],
            ticket_link=request.data["ticket_link"],
            event_image=request.data["event_image"],
            # attendees=request.data["attendees"],
            venue=venue,
            event_type=event_type
        )
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a event

        Returns:
            Response -- Empty body with 204 status code
        """

        event = Event.objects.get(pk=pk)
        event.name = request.data["name"]
        event.date = request.data["date"]
        event.doors = request.data["doors"]
        event.start_time = request.data["start_time"]
        event.details = request.data["details"]
        event.ticket_link = request.data["ticket_link"]
        event.event_image = request.data["event_image"]

        venue = Venue.objects.get(pk=request.data["venue"])
        event.venue = venue
        event_type = EventType.objects.get(pk=request.data["event_type"])
        event.event_type = event_type
        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE requests for an event

        Returns:
            Response -- Empty body with 204 status code
        """
        
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class EventVenueSerializer(serializers.ModelSerializer):
    """JSON serializer for venue
    """
    class Meta:
        model = Venue
        fields = ('id', 'name', 'location', 'admin_user')

class EventTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for event type
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
        fields = ('id', 'name', 'venue', 'date', 'doors', 'start_time', 'event_type', 'details', 'ticket_link', 'event_image')
