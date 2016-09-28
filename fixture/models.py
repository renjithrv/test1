from __future__ import unicode_literals

from django.db import models


# Fixture model for details about the fixture.
class Fixture(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gamedetails = models.ForeignKey(GameDetails)
    venue = models.ForeignKey(Venue)
    gametype = models.ForeignKey(GameType)
    level = models.ForeignKey(Level)
    gameday = models.ForeignKey(GameDay)
    gametime = models.TimeField(auto_now=False)
    courtname = models.CharField(max_length=50)
    maxplayers = models.IntegerField()
    homebatchtakein = models.IntegerField()
    homebatchstarttime = models.DurationField()
    flexibatchstarttime = models.DurationField()
    generalcutofftime = models.DurationField()
    gameversion = models.IntegerField()
    is_deleted = models.BooleanField()


class Log(models.Model):
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
    bookingid = models.ForeignKey(Booking.Log)
    fixture = models.ForeignKey(Fixture)
    buddy = models.ForeignKey(Buddy)
    teamname = models.CharField(max_length=50)
    ratingflag = models.BooleanField()

class BuddyRating(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bookingid = models.ForeignKey(Booking.Log)
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