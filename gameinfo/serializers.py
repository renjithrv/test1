from rest_framework import serializers

from gameinfo.models import Details, Type, Level, Day


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type



class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day




