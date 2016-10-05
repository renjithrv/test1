from django.db import models

# Create your models here.
class Details(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gamename = models.CharField(max_length=100)

class Type(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    typename = models.CharField(max_length=100)
    gamedetails = models.ForeignKey(Details)

class Level(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    levelname = models.CharField(max_length=100)
    gamedetails = models.ForeignKey(Details)

class Day(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dayname = models.CharField(max_length=100)


class Position(models.Model):
    POSITION_CHOICES = (('NONE', 'None'),('FORWARD', 'Forward'), ('DEFENDER', 'Defender'), ('GOALKEEPER', 'Goalkeeper'), ('MIDFIELDER', 'Midfielder'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    position = models.CharField(max_length=100,choices=POSITION_CHOICES, default='NONE')
    gamedetails = models.ForeignKey(Details)






