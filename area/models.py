from __future__ import unicode_literals
from django.db import models

# Create your models here.
class LogicalArea(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    areaname = models.CharField(max_length=100)
    areacity = models.CharField(max_length=100)

# class AreavenueTag(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     logicalarea = models.ForeignKey(LogicalArea)
#     venuedetails = models.ForeignKey(VenueDetails)