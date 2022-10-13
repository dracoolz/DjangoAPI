from pickle import TRUE
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import buses, buses_user, users
from .serializers import busesSerializer,busesUserSerializer, userSerializer

# GET
#buses
@api_view(['GET'])
def getData_buses(request):
    items = buses.objects.all()
    serializer_buses = busesSerializer(items, many=TRUE)
    return Response(serializer_buses.data)

#buses_user
@api_view(['GET'])
def getData_buses_user(request):
    items = buses_user.objects.all()
    serializer_buses_users = busesUserSerializer(items, many=TRUE)
    return Response(serializer_buses_users.data)

#user
@api_view(['GET'])
def getData_user(request):
    items = users.objects.all()
    serializer_users = userSerializer(items, many=TRUE)
    return Response(serializer_users.data)

###################################################################################
# POST
#buses
@api_view(['POST'])
def addItem_buses(request):
    serializer_buses = busesSerializer(data=request.data)
    if serializer_buses.is_valid():
        serializer_buses.save()
    return Response(serializer_buses.data)

#buses_user
@api_view(['POST'])
def addItem_buses_user(request):
    serializer_buses_user = busesUserSerializer(data=request.data)
    if serializer_buses_user.is_valid():
        serializer_buses_user.save()
    return Response(serializer_buses_user.data)

#user
@api_view(['POST'])
def addItem_user(request):
    serializer_user = userSerializer(data=request.data)
    if serializer_user.is_valid():
        serializer_user.save()
    return Response(serializer_user.data)