from rest_framework import serializers 
from users.models import Users
from groups.models import Groups
from family.models import Family
from groups.serializers import GroupSerializer
from family.serializers import FamilySerializer

 
class UserSerializer(serializers.ModelSerializer):
    # Group
    group = serializers.PrimaryKeyRelatedField(queryset=Groups.objects.all(), source="group_id", write_only=True)
    group_id = GroupSerializer(read_only=True)
    
    # Family
    family = serializers.PrimaryKeyRelatedField(queryset=Family.objects.all(), source="family_id", write_only=True)
    family_id = FamilySerializer(read_only=True)

    class Meta:
        model = Users
        fields = '__all__'



        