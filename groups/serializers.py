from rest_framework import serializers 
from groups.models import Groups
 
 
class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups
        fields = '__all__'