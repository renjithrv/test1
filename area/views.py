from django.shortcuts import render

# Create your views here.

from area.models import LogicalArea
from area.serializers import LogicalAreaSerializer


from rest_framework import serializers, viewsets

# ViewSets define the view behavior.
class AreaViewSet(viewsets.ModelViewSet):
    queryset = LogicalArea.objects.all()
    serializer_class = LogicalAreaSerializer

