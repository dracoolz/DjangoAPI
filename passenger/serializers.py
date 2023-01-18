from rest_framework import serializers 
from passenger.models import Passenger
from operation.models import Operation
from users.models import Users
from operation.serializers import OperationSerializer
from users.serializers import UserSerializer
 
class PassengerSerializer(serializers.ModelSerializer):
    # Operation
    operation_id = serializers.PrimaryKeyRelatedField(queryset=Operation.objects.all(), source="operation", write_only=True)
    operation = OperationSerializer(read_only=True)
    
    # Users
    user_id = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all(), source="user", write_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Passenger
        fields = '__all__'
    