from django.db import models

# Create your models here.
from gameinfo.models import Details
from booking.models import BookingLog


class Role(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rolename = models.CharField(max_length=100)


class Buddy(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    buddyname = models.CharField(max_length=100)
    buddyemail = models.EmailField(max_length=150)
    buddycell = models.CharField(max_length=10)
    gamedetails = models.ForeignKey(Details)
    role = models.ForeignKey(Role)




class BuddyRating(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bookingid = models.ForeignKey(BookingLog)
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