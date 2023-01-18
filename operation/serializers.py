from rest_framework import serializers 
from operation.models import Operation
from buses.models import Buses
from buses.serializers import BusSerializer
 
 
class OperationSerializer(serializers.ModelSerializer):
    # Bus
    bus_id = serializers.PrimaryKeyRelatedField(queryset=Buses.objects.all(), source="bus", write_only=True)
    bus = BusSerializer(read_only=True)
    
    class Meta:
        model = Operation
        fields = '__all__'
    