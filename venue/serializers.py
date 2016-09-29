from rest_framework import serializers

from venue.models import VenueDetails,VenueGamesAvailable


class VenueDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueDetails



class VenueGamesAvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueGamesAvailable







