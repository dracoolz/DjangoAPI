#this serializer is for serailize the data before render it out, because response onject connot 
# natively handle complex data type such as django model instances.
from rest_framework import serializers
from base.models import buses, buses_user, users

#buses
class busesSerializer(serializers.ModelSerializer):
    class Meta:
        model = buses
        fields = '__all__'

#buses-user
class busesUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = buses_user
        fields = '__all__'

#user
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'