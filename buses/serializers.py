from rest_framework import serializers 
from buses.models import Buses
from groups.serializers import GroupSerializer
 
 
class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buses
        fields = '__all__'
    
    # retrieve data from relation
    group_id = GroupSerializer()