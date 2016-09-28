from django.shortcuts import render

# Create your views here.

from customer.models import Play_customer_profile,Improve_customer_profile,Initial_customer_profile
from customer.serializers import Play_customer_Serializer,Improve_customer_Serializer,Initial_customer_Serializer


from rest_framework import serializers, viewsets

# ViewSets define the view behavior.
class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play_customer_profile.objects.all()
    serializer_class = Play_customer_Serializer

    # ViewSets define the view behavior.
class ImproveViewSet(viewsets.ModelViewSet):
    queryset = Improve_customer_profile.objects.all()
    serializer_class = Improve_customer_Serializer


    # ViewSets define the view behavior.
class InitialViewSet(viewsets.ModelViewSet):
    queryset = Initial_customer_profile.objects.all()
    serializer_class = Initial_customer_Serializer
