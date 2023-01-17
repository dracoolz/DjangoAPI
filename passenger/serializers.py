from rest_framework import serializers 
from passenger.models import Passenger
from operation.models import Operation
from users.models import Users
from operation.serializers import OperationSerializer
from users.serializers import UserSerializer
 
class PassengerSerializer(serializers.ModelSerializer):
    # Operation
    operation = serializers.PrimaryKeyRelatedField(queryset=Operation.objects.all(), source="operation_id", write_only=True)
    operation_id = OperationSerializer(read_only=True)
    
    # Users
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all(), source="user_id", write_only=True)
    user_id = UserSerializer(read_only=True)
    
    class Meta:
        model = Passenger
        fields = '__all__'
    