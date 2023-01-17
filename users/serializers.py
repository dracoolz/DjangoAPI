from rest_framework import serializers 
from users.models import Users
from groups.models import Groups
from family.models import Family
from groups.serializers import GroupSerializer
from family.serializers import FamilySerializer

 
class UserSerializer(serializers.ModelSerializer):
    # # Group
    # group = GroupSerializer(read_only=True)
    # group_id = serializers.PrimaryKeyRelatedField(queryset=Groups.objects.all(), write_only=True)
    
    # # Family
    # family = FamilySerializer(read_only=True)
    # family_id = serializers.PrimaryKeyRelatedField(queryset=Family.objects.all(), write_only=True)

    class Meta:
        model = Users
        fields = '__all__'



        