from django.shortcuts import render

# Create your views here.

from payment.models import PaymentDetails
from payment.serializers import PaymentDetailsSerializer


from rest_framework import serializers, viewsets

# ViewSets define the view behavior.
class PaymentDetailsViewSet(viewsets.ModelViewSet):
    queryset = PaymentDetails.objects.filter(id=1)
    serializer_class = PaymentDetailsSerializer









