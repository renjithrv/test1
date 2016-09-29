from rest_framework import serializers

from booking.models import Log, FootballPlayProgress, FootballImproveProgress


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log


class FootballPlayProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballPlayProgress



class FootballImproveProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballImproveProgress


