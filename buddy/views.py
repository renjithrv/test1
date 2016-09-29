from django.shortcuts import render

# Create your views here.

from buddy.models import Buddy,Role
from buddy.serializers import BuddyDetailsSerializer,RoleSerializer



from rest_framework import serializers, viewsets

# ViewSets define the view behavior.
class BuddyViewSet(viewsets.ModelViewSet):
    queryset = Buddy.objects.all()
    serializer_class = BuddyDetailsSerializer



# ViewSets define the view behavior.
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer




