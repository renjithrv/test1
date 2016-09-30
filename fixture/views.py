from django.shortcuts import render

# Create your views here.

from fixture.models import Fixture,BuddyAudit,AssignedBuddy,AssignedBuddyLog
from fixture.serializers import FixtureSerializer,BuddyAuditSerializer,AssignedBuddySerializer,AssignedBuddyLogSerializer



from rest_framework import serializers, viewsets

# ViewSets define the view behavior.
class FixtureViewSet(viewsets.ModelViewSet):
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer



# ViewSets define the view behavior.
class BuddyAuditViewSet(viewsets.ModelViewSet):
    queryset = BuddyAudit.objects.all()
    serializer_class = BuddyAuditSerializer


# ViewSets define the view behavior.
class AssignedBuddyViewSet(viewsets.ModelViewSet):
    queryset = AssignedBuddy.objects.all()
    serializer_class = AssignedBuddySerializer



# ViewSets define the view behavior.
class AssignedBuddyLogViewSet(viewsets.ModelViewSet):
    queryset = AssignedBuddyLog.objects.all()
    serializer_class = AssignedBuddyLogSerializer










