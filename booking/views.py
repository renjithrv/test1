from django.shortcuts import render

# Create your views here.

from booking.models import BookingLog,FootballPlayProgress,FootballImproveProgress
from booking.serializers import LogSerializer,FootballPlayProgressSerializer,FootballImproveProgressSerializer


from rest_framework import serializers, viewsets

# ViewSets define the view behavior.
class BookingLogViewSet(viewsets.ModelViewSet):
    queryset = BookingLog.objects.all()
    serializer_class = LogSerializer



# ViewSets define the view behavior.
class FootballPlayProgressViewSet(viewsets.ModelViewSet):
    queryset = FootballPlayProgress.objects.all()
    serializer_class = FootballPlayProgressSerializer



# ViewSets define the view behavior.
class FootballImproveProgressViewSet(viewsets.ModelViewSet):
    queryset = FootballImproveProgress.objects.all()
    serializer_class = FootballImproveProgressSerializer

