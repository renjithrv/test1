from rest_framework import serializers

from fixture.models import Fixture, BuddyAudit, AssignedBuddy, AssignedBuddyLog


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





