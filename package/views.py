from django.shortcuts import render

# Create your views here.

from package.models import Package
from package.serializers import PackageSerializer


from rest_framework import serializers, viewsets

# ViewSets define the view behavior.
class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer









