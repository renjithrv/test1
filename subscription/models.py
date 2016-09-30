from django.db import models

# Create your models here.


class Subscription(models.Model):
    customer = models.ForeignKey('customer.Customer')
    package = models.ForeignKey('package.Package')
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    startdate = models.DateField(max_length=255, null=False)
    enddate = models.DateField(max_length=255, null=False)
    sessionsleft = models.IntegerField()
    flexiflag = models.BooleanField()
    expiryflag = models.BooleanField()
