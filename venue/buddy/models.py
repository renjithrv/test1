from django.db import models

# Create your models here.
from gameinfo.models import GameDetails


class Buddy(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    buddyname = models.CharField(max_length=100)
    buddyemail = models.EmailField(max_length=254)
    buddycell = models.CharField(max_length=10)
    gamedetails = models.ForeignKey(GameDetails)
    role = models.ForeignKey(Role)

class Role(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rolename = models.CharField(max_length=100)