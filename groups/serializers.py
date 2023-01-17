from rest_framework import serializers 
from groups.models import Groups
from buses.models import Buses
from buses.serializers import BusSerializer
 
class GroupSerializer(serializers.ModelSerializer):
    # Bus
    bus = serializers.PrimaryKeyRelatedField(queryset=Buses.objects.all(), source="bus_id", write_only=True)
    bus_id = BusSerializer(read_only=True)
    
    class Meta:
        model = Groups
        fields = '__all__'