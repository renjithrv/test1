from rest_framework import serializers

from customer.models import Customer, CustomerLog, GamePreference, Subscription, GameLevel


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer


class CustomerLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerLog



class GamePreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePreference


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription


class GameLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameLevel


