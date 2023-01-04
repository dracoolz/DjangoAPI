from rest_framework import serializers 
from operation.models import Operation
from buses.serializers import BusSerializer
 
 
class OperationSerializer(serializers.ModelSerializer):
    # retrieve data from relation
    # bus_id = BusSerializer()
    
    class Meta:
        model = Operation
        fields = '__all__'
    