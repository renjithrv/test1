from rest_framework import serializers
from buddy.models import Buddy,Role

class BuddyDetailsSerializer(serializers.ModelSerializer):
    class Meta :
        model = Buddy
        fields = ('id','buddyname','buddyemail','buddycell',)


class RoleSerializer(serializers.ModelSerializer):
    class Meta :
        model = Role