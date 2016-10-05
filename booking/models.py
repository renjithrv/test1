from django.db import models

from customer.models import Customer


# Create your models here.

class BookingLog(models.Model):
    BATCH_TYPE_CHOICES = (('HOME', 'Home'), ('FLEXI', 'Flexi'), ('DEMO', 'Demo'))
    customer = models.ForeignKey(Customer)
    fixture = models.ForeignKey('fixture.Fixture')
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    updated_on = models.DateTimeField(auto_now=True, null=False)
    booked_date = models.DateField(max_length=255, null=False)
    game_date = models.DateField(max_length=255, null=False)
    join_status = models.BooleanField()
    batch_type = models.CharField(max_length=8, choices=BATCH_TYPE_CHOICES, default='HOME')


class FootballPlayProgress(models.Model):
    bookinglog = models.ForeignKey(BookingLog)
    #customer
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    game_week = models.IntegerField()
    passing = models.IntegerField()
    receiving = models.IntegerField()
    dribbling = models.IntegerField()
    defending = models.IntegerField()
    attacking = models.IntegerField()

    teamname = models.CharField(max_length=10)
    goalfor = models.IntegerField()
    goalagainst = models.IntegerField()

    team = models.ForeignKey(Team)

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
    processedflag = models.BooleanField()

class Team(models.Model):
    name = models.CharField(max_length=32)
    customers = models.ManyToManyField(Customer)

class TeamGameLog(models.Model):
    goal_scored = models.PositiveIntegerField(default=0)
    team = models.ForeignKey(Team)
    game = models.ForeignKey(Game)
    booking = models.ForeignKey(BookingLog)

class Game(models.Model):
    team1 = models.ForeignKey(Team)
    team2 = models.ForeignKey(Team)

    created_on = models.DateTimeField()


class FootballImproveProgress(models.Model):
    FLEX_NONE = "NONE"
    FLEXIBILITY_TYPE_CHOICES = (
        (FLEX_NONE, 'Not Taken'), ('POOR', 'Poor'), ('AVERAGE', 'Average'), ('GOOD', 'Good'), ('EXCELLENT', 'Excellent'))
    bookinglog = models.ForeignKey(BookingLog)
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
    flexibility = models.CharField(max_length=15, choices=FLEXIBILITY_TYPE_CHOICES, default=FLEX_NONE)

