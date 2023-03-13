"""View module for handling requests about event types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from backendapi.models import EventType


class EventTypeView(ViewSet):
    """36one5 event types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event type

        Returns:
            Response -- JSON serialized event type
        """
        event_type = EventType.objects.get(pk=pk)
        serializer = EventTypeSerializer(event_type)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all event types

        Returns:
            Response -- JSON serialized list of event types
        """
        event_types = EventType.objects.all()
        serializer = EventTypeSerializer(event_types, many=True)
        return Response(serializer.data)

class EventTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for event types
    """
    class Meta:
        model = EventType
        fields = ('id', 'label')
