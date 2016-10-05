from django.shortcuts import render

# Create your views here.

from gameinfo.models import Details,Type,Level,Day,Position
from gameinfo.serializers import DetailsSerializer,TypeSerializer,LevelSerializer,DaySerializer,PositionSerializer



from rest_framework import serializers, viewsets

# ViewSets define the view behavior.
class DetailsViewSet(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer



# ViewSets define the view behavior.
class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


# ViewSets define the view behavior.
class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer



# ViewSets define the view behavior.
class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


# ViewSets define the view behavior.
class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer






