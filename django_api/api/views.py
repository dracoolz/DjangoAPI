from pickle import TRUE
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import buses, buses_user, users
from .serializers import ItemSerializer

# GET
#buses
@api_view(['GET'])
def getData_buses(request):
    items = buses.objects.all()
    serializer_buses = ItemSerializer(items, many=TRUE)
    return Response(serializer_buses.data)

#buses_user
@api_view(['GET'])
def getData_buses_user(request):
    items = buses_user.objects.all()
    serializer_buses = ItemSerializer(items, many=TRUE)
    return Response(serializer_buses.data)

#user
@api_view(['GET'])
def getData_user(request):
    items = users.objects.all()
    serializer_buses = ItemSerializer(items, many=TRUE)
    return Response(serializer_buses.data)


# POST
@api_view(['POST'])
def addItem(request):
    serializer_buses = ItemSerializer(data=request.data)
    if serializer_buses.is_valid():
        serializer_buses.save()
    return Response(serializer_buses.data)