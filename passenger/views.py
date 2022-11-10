from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from passenger.models import Passenger
from passenger.serializers import PassengerSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def passenger_list(request):
    if request.method == 'GET':
        passenger = Passenger.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            passenger = passenger.filter(title__icontains=title)
        
        passenger_serializer = PassengerSerializer(passenger, many=True)
        return JsonResponse(passenger_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        family_data = JSONParser().parse(request)
        passenger_serializer = PassengerSerializer(data=family_data)
        if passenger_serializer.is_valid():
            passenger_serializer.save()
            return JsonResponse(passenger_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(passenger_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Passenger.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def passenger_detail(request, pk):
    try: 
        passenger = Passenger.objects.get(pk=pk) 
    except Passenger.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        passenger_serializer = PassengerSerializer(passenger) 
        return JsonResponse(passenger_serializer.data) 
 
    elif request.method == 'PUT': 
        passenger_data = JSONParser().parse(request) 
        passenger_serializer = PassengerSerializer(passenger, data=passenger_data) 
        if passenger_serializer.is_valid(): 
            passenger_serializer.save() 
            return JsonResponse(passenger_serializer.data) 
        return JsonResponse(passenger_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        passenger.delete() 
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def passenger_list_published(request):
    passenger = Passenger.objects.filter(published=True)
        
    if request.method == 'GET': 
        passenger_serializer = PassengerSerializer(passenger, many=True)
        return JsonResponse(passenger_serializer.data, safe=False)
    
