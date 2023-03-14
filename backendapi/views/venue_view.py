"""View module for handling requests about venues"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from backendapi.models import Venue, Profile


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
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized event instance
        """

        try:
            admin_user = Profile.objects.get(user=request.auth.user)
        except Profile.DoesNotExist:
            return Response({'message': 'You sent an invalid token'}, status=status.HTTP_404_NOT_FOUND)

        venue = Venue.objects.create(
            name=request.data["name"],
            location=request.data["location"],
            hours=request.data["hours"],
            details=request.data["details"],
            coordinates=request.data["coordinates"],
            website=request.data["website"],
            venue_image=request.data["venue_image"],
            admin_user=admin_user,
        )
        serializer = VenueSerializer(venue)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a venue

        Returns:
            Response -- Empty body with 204 status code
        """

        venue = Venue.objects.get(pk=pk)
        venue.name = request.data["name"]
        venue.location = request.data["location"]
        venue.hours = request.data["hours"]
        venue.details = request.data["details"]
        venue.coordinates = request.data["coordinates"]
        venue.website = request.data["website"]
        venue.venue_image = request.data["venue_image"]
        venue.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE requests for an venue

        Returns:
            Response -- Empty body with 204 status code
        """
        
        venue = Venue.objects.get(pk=pk)
        venue.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


# class UserSerializer(serializers.ModelSerializer):
#     """JSON serializer for user
#     """
#     class Meta:
#         model = User
#         fields = ('id', 'first_name', 'last_name', 'username', 'email', 'date_joined', 'is_staff')

class ProfileSerializer(serializers.ModelSerializer):
    """JSON serializer for profile
    """
    class Meta:
        model = Profile
        fields = ('id', 'user', 'bio')

class VenueSerializer(serializers.ModelSerializer):
    """JSON serializer for venues
    """
    admin_user = ProfileSerializer(many=False)

    class Meta:
        model = Venue
        fields = ('id', 'name', 'location', 'admin_user', 'hours', 'details', 'coordinates', 'website', 'venue_image')
