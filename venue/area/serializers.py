from rest_framework import serializers

from area.models import LogicalArea

class LogicalAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogicalArea
        fields = ('id','areaname','areacity')
