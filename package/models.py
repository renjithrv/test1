from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Package(models.Model):
   customer = models.ForeignKey(Customer)
   gamedetail = models.ForeignKey(GameDetails)
   created_at = models.DateTimeField(auto_now_add=True, null=False)
   updated_at = models.DateTimeField(auto_now=True, null=False)
   name = models.CharField(max_length=255, null=False)
   amount = models.IntegerField()
   duration = models.DurationField()
   enableflag = models.BooleanField()
