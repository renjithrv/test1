from django.shortcuts import render

# Create your views here.

from subscription.models import Subscription
from subscription.serializers import SubscriptionSerializer



from rest_framework import serializers, viewsets





# ViewSets define the view behavior.
class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer






