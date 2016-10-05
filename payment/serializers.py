from rest_framework import serializers

from payment.models import PaymentDetails


class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails






