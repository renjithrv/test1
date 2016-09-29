from __future__ import unicode_literals

from django.db import models

from booking.models import Log
from buddy.models import Buddy
from package.models import Package
from gameinfo.models import Details,Day,Type,Level
from area.models import LogicalArea
from venue.models import VenueDetails,VenueGamesAvailable


# Fixture model for details about the fixture.
class Fixture(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gamedetails = models.ForeignKey(Details)
    venue = models.ForeignKey(VenueDetails)
    gametype = models.ForeignKey(Type)
    level = models.ForeignKey(Level)
    gameday = models.ForeignKey(Day)
    gametime = models.TimeField(auto_now=False)
    courtname = models.CharField(max_length=50)
    maxplayers = models.IntegerField()
    homebatchtakein = models.IntegerField()
    homebatchstarttime = models.DurationField()
    flexibatchstarttime = models.DurationField()
    generalcutofftime = models.DurationField()
    gameversion = models.IntegerField()
    is_deleted = models.BooleanField()


class BuddyAudit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    fixture = models.ForeignKey(Fixture)
    buddy = models.ForeignKey(Buddy)
    starttime = models.TimeField(auto_now=False)
    endtime = models.TimeField(auto_now=False)
    startlatitude = models.DecimalField(max_digits=10, max_length=8)
    startlongitude = models.DecimalField(max_digits=11, max_length=8)
    endlatitude = models.DecimalField(max_digits=10, max_length=8)
    endlongitude = models.DecimalField(max_digits=11, max_length=8)

class AssignedBuddy(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    fixture = models.ForeignKey(Fixture)
    buddy = models.ForeignKey(Buddy)
    tempbuddy = models.ForeignKey(Buddy)

class AssignedBuddyLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bookingid = models.ForeignKey(Log)
    fixture = models.ForeignKey(Fixture)
    buddy = models.ForeignKey(Buddy)
    teamname = models.CharField(max_length=50)
    ratingflag = models.BooleanField()

class BuddyRating(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bookingid = models.ForeignKey(Log)
    sessionrating = models.IntegerField()
    timemanagement = models.BooleanField()
    warmup = models.BooleanField()
    matchquality = models.BooleanField()
    sessionissues = models.BooleanField()
    sessioncomments = models.TextField()
    buddy = models.ForeignKey(Buddy)
    buddyrating = models.IntegerField()
    communication = models.BooleanField()
    attire = models.BooleanField()
    gameknowledge = models.BooleanField()
    buddyissue = models.BooleanField()
    buddycomments = models.TextField()