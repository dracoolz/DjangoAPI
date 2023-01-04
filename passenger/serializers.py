from rest_framework import serializers 
from passenger.models import Passenger
from operation.serializers import OperationSerializer
from users.serializers import UserSerializer
 
class PassengerSerializer(serializers.ModelSerializer):
    # retrieve data from relation
    # operation_id = OperationSerializer()
    # user_id = UserSerializer()
    
    class Meta:
        model = Passenger
        fields = '__all__'
    