from rest_framework import serializers 
from users.models import Users
from groups.serializers import GroupSerializer
from family.serializers import FamilySerializer
 
class UserSerializer(serializers.ModelSerializer):
    # retrieve data from relation
    # group_id = GroupSerializer()
    # family_id = FamilySerializer()
    
    class Meta:
        model = Users
        fields = '__all__'
        