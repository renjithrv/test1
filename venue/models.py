from __future__ import unicode_literals

from django.db import models

# Create your models here.
from area.models import LogicalArea
from gameinfo.models import Details


class VenueDetails(models.Model) :
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    venuename = models.CharField(max_length=100)
    venuepic = models.ImageField()
    latitude = models.DecimalField(max_digits=10,max_length=8)
    longitude = models.DecimalField(max_digits=11,max_length=8)
    logicalarea = models.ForeignKey(LogicalArea)

class VenueGamesAvailable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    venuedetails = models.ForeignKey(VenueDetails)
    gamedetails = models.ForeignKey(Details)

