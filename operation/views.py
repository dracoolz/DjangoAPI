from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from operation.models import Operation
from operation.serializers import OperationSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def operation_list(request):
    if request.method == 'GET':
        operation = Operation.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            operation = operation.filter(title__icontains=title)
        
        operation_serializer = OperationSerializer(operation, many=True)
        return JsonResponse(operation_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        operation_data = JSONParser().parse(request)
        operation_serializer = OperationSerializer(data=operation_data)
        if operation_serializer.is_valid():
            operation_serializer.save()
            return JsonResponse(operation_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(operation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Operation.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def operation_detail(request, pk):
    try: 
        operation = Operation.objects.get(pk=pk) 
    except Operation.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        operation_serializer = OperationSerializer(operation) 
        return JsonResponse(operation_serializer.data) 
 
    elif request.method == 'PUT': 
        operation_data = JSONParser().parse(request) 
        operation_serializer = OperationSerializer(operation, data=operation_data) 
        if operation_serializer.is_valid(): 
            operation_serializer.save() 
            return JsonResponse(operation_serializer.data) 
        return JsonResponse(operation_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        operation.delete() 
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def operation_list_published(request):
    operation = Operation.objects.filter(published=True)
        
    if request.method == 'GET': 
        operation_serializer = OperationSerializer(operation, many=True)
        return JsonResponse(operation_serializer.data, safe=False)
    
