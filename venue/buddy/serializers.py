from rest_framework import serializers
from buddy.models import BuddyDetails

class BuddyDetailsSerialize(serializers.ModelSerializer):
    class Meta :
        model = BuddyDetails
        fields = ('id','buddyname','buddyemail','buddycell',)