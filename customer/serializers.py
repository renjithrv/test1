from rest_framework import serializers

from customer.models import Customer, CustomerLog, GamePreference, GameLevel


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('firstname','lastname','mobile','email','customerpic')


class CustomerLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerLog



class GamePreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePreference



class GameLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameLevel


