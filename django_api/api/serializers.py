#this serializer is for serailize the data before render it out, because response onject connot 
# natively handle complex data type such as django model instances.
from rest_framework import serializers
from base.models import buses

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = buses
        fields = '__all__'