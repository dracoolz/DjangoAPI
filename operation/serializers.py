from rest_framework import serializers 
from operation.models import Operation
from buses.serializers import BusSerializer
 
 
class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'
    
    # retrieve data from relation
    bus_id = BusSerializer()