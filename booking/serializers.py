from rest_framework import serializers

from booking.models import BookingLog, FootballPlayProgress, FootballImproveProgress
from customer.serializers import CustomerSerializer



class LogSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = BookingLog
        fields = ('customer','fixture','joinstatus','gamedate','batchtype')



class FootballPlayProgressSerializer(serializers.ModelSerializer):
    bookinglog = LogSerializer()
    class Meta:
        model = FootballPlayProgress
        fields = ('bookinglog','matchpoints')






class FootballImproveProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballImproveProgress


