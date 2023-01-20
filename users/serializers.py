from rest_framework import serializers 
from users.models import Users
from groups.models import Groups
from family.models import Family
from groups.serializers import GroupSerializer
from family.serializers import FamilySerializer

 
class UserSerializer(serializers.ModelSerializer):
    # Group
    group_id = serializers.PrimaryKeyRelatedField(queryset=Groups.objects.all(), source="group", allow_null=True, write_only=True)
    group = GroupSerializer(read_only=True)
    
    # Family
    family_id = serializers.PrimaryKeyRelatedField(queryset=Family.objects.all(), source="family", allow_null=True, write_only=True)
    family = FamilySerializer(read_only=True)

    class Meta:
        model = Users
        fields = '__all__'



        