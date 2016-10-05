from rest_framework import serializers

from leads.models import LeadDetails


class LeadDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadDetails





