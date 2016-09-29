from __future__ import unicode_literals

from django.db import models

from customer.models import Customer
from gameinfo.models import GameDetails
from fixture.models import Fixture



# Create your models here.

class Log(models.Model):
   BATCH_TYPE_CHOICES = (
      (HOME, 'Home'),
      (FLEXI, 'Flexi'),
      (DEMO, 'Demo')
    )

   customer = models.ForeignKey(Customer)
   gamedetail = models.ForeignKey(GameDetails)
   fixture = models.ForeignKey(Fixture)
   created_at = models.DateTimeField(auto_now_add=True, null=False)
   updated_at = models.DateTimeField(auto_now=True, null=False)
   bookeddate = models.DateField(max_length=255, null=False)
   gamedate = models.DateField(max_length=255, null=False)
   joinstatus = models.BooleanField()
   batchtype = models.CharField(max_length=8, choices=BATCH_TYPE_CHOICES, default=HOME)
 



class FootballPlayProgress(models.Model):
   bookinglog = models.ForeignKey(Log)
   created_at = models.DateTimeField(auto_now_add=True, null=False)
   updated_at = models.DateTimeField(auto_now=True, null=False)
   gameweek = models.IntegerField()
   passing = models.IntegerField()
   receiving = models.IntegerField()
   dribbling = models.IntegerField()
   defending = models.IntegerField()
   attacking = models.IntegerField()
   teamname = models.CharField(max_length=10)
   goalfor = models.IntegerField()
   goalagainst = models.IntegerField()
   goals = models.IntegerField()
   goalpoints = models.IntegerField()
   assists = models.IntegerField()
   assistpoints = models.IntegerField()
   goalconceded = models.IntegerField()
   cleansheet = models.IntegerField()
   resultpoints = models.IntegerField()
   bonuspoints = models.IntegerField()
   matchpoints = models.IntegerField()
   formmeter = models.IntegerField()
   processedflag = models.BooleanField(max_length=4)



class FootballImproveProgress(models.Model):
   FLEXIBILITY_TYPE_CHOICES = (
      (NONE, 'Not Taken'),
      (POOR, 'Poor'),
      (AVERAGE, 'Average'),
      (GOOD, 'Good'),
      (EXCELLENT, 'Excellent')
    )
   bookinglog = models.ForeignKey(Log)
   created_at = models.DateTimeField(auto_now_add=True, null=False)
   updated_at = models.DateTimeField(auto_now=True, null=False)
   gameweek = models.IntegerField()
   passing = models.IntegerField()
   receiving = models.IntegerField()
   dribbling = models.IntegerField()
   defending = models.IntegerField()
   attacking = models.IntegerField()
   teamname = models.CharField(max_length=10)
   goalfor = models.IntegerField()
   goalagainst = models.IntegerField()
   goals = models.IntegerField()
   goalpoints = models.IntegerField()
   assists = models.IntegerField()
   assistpoints = models.IntegerField()
   upperbody = models.IntegerField()
   lowerbody = models.IntegerField()
   core = models.IntegerField()
   weight = models.IntegerField()
   flexibility = models.CharField(max_length=15, choices=FLEXIBILITY_TYPE_CHOICES, default=NONE)
