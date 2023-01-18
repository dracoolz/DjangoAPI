from rest_framework import serializers 
from groups.models import Groups
from buses.models import Buses
from buses.serializers import BusSerializer
 
class GroupSerializer(serializers.ModelSerializer):
    # Bus
    bus_id = serializers.PrimaryKeyRelatedField(queryset=Buses.objects.all(), source="bus", write_only=True)
    bus = BusSerializer(read_only=True)
    
    class Meta:
        model = Groups
        fields = '__all__'