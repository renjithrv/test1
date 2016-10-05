from django.db import models


class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    mobile = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=255, blank=True, null=True)
    customerpic = models.ImageField()


class CustomerLog(models.Model):
    customer = models.ForeignKey(Customer)
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class GamePreference(models.Model):
    customer = models.ForeignKey(Customer)
    gameday = models.ForeignKey('gameinfo.Day')
    fixture = models.ForeignKey('fixture.Fixture')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GameLevel(models.Model):
    customer = models.ForeignKey(Customer)
    gamedetail = models.ForeignKey('gameinfo.Details')
    gamelevel = models.ForeignKey('gameinfo.Level')
    gameposition = models.ForeignKey('gameinfo.Position')
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
