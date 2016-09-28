from rest_framework import serializers
from venue.models import VenueDetails

class VenueDetailsSerializer(serializers.ModelSerializer):
    class Meta :
        models = VenueDetails
        fields = ('id','venuename','venuepic','latitude','longitude')


