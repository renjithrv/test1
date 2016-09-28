from django.db import models

# Create your models here.
class GameDetails(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gamename = models.CharField(max_length=100)

class GameType (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    typename = models.CharField(max_length=100)
    gamedetails = models.ForeignKey(GameDetails)

class GameLevel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    levelname = models.CharField(max_length=100)
    gamedetails = models.ForeignKey(GameDetails)

class GameDay(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dayname = models.CharField(max_length=100)

