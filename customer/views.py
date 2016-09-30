from django.shortcuts import render

# Create your views here.

from customer.models import Customer,CustomerLog,GamePreference,GameLevel
from customer.serializers import CustomerSerializer,CustomerLogSerializer,GamePreferenceSerializer,GameLevelSerializer



from rest_framework import serializers, viewsets

# ViewSets define the view behavior.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer



# ViewSets define the view behavior.
class CustomerLogViewSet(viewsets.ModelViewSet):
    queryset = CustomerLog.objects.all()
    serializer_class = CustomerLogSerializer


# ViewSets define the view behavior.
class GamePreferenceViewSet(viewsets.ModelViewSet):
    queryset = GamePreference.objects.all()
    serializer_class = GamePreferenceSerializer



# ViewSets define the view behavior.
class GameLevelViewSet(viewsets.ModelViewSet):
    queryset = GameLevel.objects.all()
    serializer_class = GameLevelSerializer







