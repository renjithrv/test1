

from django.db import models

# Create your models here.

from gameinfo.models import Details


class Package(models.Model):
   gamedetail = models.ForeignKey(Details)
   created_at = models.DateTimeField(auto_now_add=True, null=False)
   updated_at = models.DateTimeField(auto_now=True, null=False)
   name = models.CharField(max_length=255, null=False)
   amount = models.IntegerField()
   sessions = models.IntegerField()
   duration = models.DurationField()
   enableflag = models.BooleanField()
