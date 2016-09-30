from django.shortcuts import render

# Create your views here.

from buddy.models import Buddy,Role,BuddyRating
from buddy.serializers import BuddyDetailsSerializer,RoleSerializer,BuddyRatingSerializer



from rest_framework import serializers, viewsets

# ViewSets define the view behavior.
class BuddyViewSet(viewsets.ModelViewSet):
    queryset = Buddy.objects.all()
    serializer_class = BuddyDetailsSerializer



# ViewSets define the view behavior.
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


# ViewSets define the view behavior.
class BuddyRatingViewSet(viewsets.ModelViewSet):
    queryset = BuddyRating.objects.all()
    serializer_class = BuddyRatingSerializer








