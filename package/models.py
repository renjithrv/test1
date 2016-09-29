from __future__ import unicode_literals

from django.db import models

# Create your models here.
from customer.models import Customer
from gameinfo.models import Details


class Package(models.Model):
   customer = models.ForeignKey(Customer)
   gamedetail = models.ForeignKey(Details)
   created_at = models.DateTimeField(auto_now_add=True, null=False)
   updated_at = models.DateTimeField(auto_now=True, null=False)
   name = models.CharField(max_length=255, null=False)
   amount = models.IntegerField()
   duration = models.DurationField()
   enableflag = models.BooleanField()
