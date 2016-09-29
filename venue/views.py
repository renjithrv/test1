from django.shortcuts import render

# Create your views here.

from venue.models import VenueDetails,VenueGamesAvailable
from venue.serializers import VenueDetailsSerializer,VenueGamesAvailableSerializer


from rest_framework import serializers, viewsets

# ViewSets define the view behavior.
class VenueDetailsViewSet(viewsets.ModelViewSet):
    queryset = VenueDetails.objects.all()
    serializer_class = VenueDetailsSerializer



# ViewSets define the view behavior.
class VenueGamesAvailableViewSet(viewsets.ModelViewSet):
    queryset = VenueGamesAvailable.objects.all()
    serializer_class = VenueGamesAvailableSerializer








