from rest_framework import serializers

from fixture.models import Fixture, BuddyAudit, AssignedBuddy, AssignedBuddyLog, BuddyRating


class FixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixture


class BuddyAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuddyAudit



class AssignedBuddySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedBuddy


class AssignedBuddyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedBuddyLog


class BuddyRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuddyRating


