from __future__ import unicode_literals

from django.db import models

class Customer(models.Model):
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   name = models.CharField(max_length=100, null=False)
   mobile = models.IntegerField(max_length=10, null=False)
   email = models.EmailField(max_length=255, blank=True, null=True)
  


class Log(models.Model):
   customer = models.ForeignKey(Customer)
   created_at = models.DateTimeField(auto_now_add=True, null=False)



class GamePreference(models.Model):
   customer = models.ForeignKey(Customer)
   gamedetails = models.ForeignKey(GameDetails)
   logicalarea = models.ForeignKey(LogicalArea)
   gameday = models.ForeignKey(GameDay)
   fixture = models.ForeignKey(Fixture)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   


class Subscription(models.Model):
   customer = models.ForeignKey(Customer)
   package = models.ForeignKey(Package)
   created_at = models.DateTimeField(auto_now_add=True, null=False)
   updated_at = models.DateTimeField(auto_now=True, null=False)
   startdate = models.DateField(max_length=255, null=False)
   enddate = models.DateField(max_length=255, null=False)
   sessionsleft = models.IntegerField()
   flexiflag = models.BooleanField(default=False)
  


class GameLevel(models.Model):
   customer = models.ForeignKey(Customer)
   gamedetail = models.ForeignKey(GameDetails)
   created_at = models.DateTimeField(auto_now_add=True, null=False)
   updated_at = models.DateTimeField(auto_now=True, null=False)
