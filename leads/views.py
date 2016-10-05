from django.shortcuts import render

# Create your views here.

from leads.models import LeadDetails
from leads.serializers import LeadDetailsSerializer



from rest_framework import serializers, viewsets

# ViewSets define the view behavior.
class LeadDetailsViewSet(viewsets.ModelViewSet):
    queryset = LeadDetails.objects.all()
    serializer_class = LeadDetailsSerializer








