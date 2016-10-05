from django.db import models



class PaymentDetails(models.Model):
    STATUS_CHOICES = (('TRIED', 'Tried'), ('SUCCESS', 'Success'), ('FAILED', 'Failed'))
    customer = models.ForeignKey('customer.Customer')
    amount = models.IntegerField()
    status = models.CharField(max_length=100,choices=STATUS_CHOICES, default='NONE')
    created_at = models.DateTimeField(auto_now_add=True)




