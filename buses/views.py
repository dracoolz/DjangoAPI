from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from buses.models import Buses
from buses.serializers import BusSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def buses_list(request):
    if request.method == 'GET':
        buses = Buses.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            buses = buses.filter(title__icontains=title)
        
        bus_serializer = BusSerializer(buses, many=True)
        return JsonResponse(bus_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        bus_data = JSONParser().parse(request)
        bus_serializer = BusSerializer(data=bus_data)
        if bus_serializer.is_valid():
            bus_serializer.save()
            return JsonResponse(bus_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(bus_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Buses.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def buses_detail(request, pk):
    try: 
        bus = Buses.objects.get(pk=pk) 
    except Buses.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        bus_serializer = BusSerializer(bus) 
        return JsonResponse(bus_serializer.data) 
 
    elif request.method == 'PUT': 
        bus_data = JSONParser().parse(request) 
        bus_serializer = BusSerializer(bus, data=bus_data) 
        if bus_serializer.is_valid(): 
            bus_serializer.save() 
            return JsonResponse(bus_serializer.data) 
        return JsonResponse(bus_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        bus.delete() 
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def buses_list_published(request):
    bus = Buses.objects.filter(published=True)
        
    if request.method == 'GET': 
        bus_serializer = BusSerializer(bus, many=True)
        return JsonResponse(bus_serializer.data, safe=False)
    
