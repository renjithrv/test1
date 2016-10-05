from django.db import models



class LeadDetails(models.Model):
    customer = models.ForeignKey('customer.Customer')
    gamedetails = models.ForeignKey('gameinfo.Details')
    couponcode = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    leadgeneratedtime = models.DateTimeField(auto_now_add=True)







