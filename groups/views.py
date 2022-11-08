from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from groups.models import Groups
from groups.serializers import GroupSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def group_list(request):
    if request.method == 'GET':
        groups = Groups.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            groups = groups.filter(title__icontains=title)
        
        group_serializer = GroupSerializer(groups, many=True)
        return JsonResponse(group_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        group_data = JSONParser().parse(request)
        group_serializer = GroupSerializer(data=group_data)
        if group_serializer.is_valid():
            group_serializer.save()
            return JsonResponse(group_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(group_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Groups.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def group_detail(request, pk):
    try: 
        group = Groups.objects.get(pk=pk) 
    except Groups.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        group_serializer = GroupSerializer(group) 
        return JsonResponse(group_serializer.data) 
 
    elif request.method == 'PUT': 
        group_data = JSONParser().parse(request) 
        group_serializer = GroupSerializer(group, data=group_data) 
        if group_serializer.is_valid(): 
            group_serializer.save() 
            return JsonResponse(group_serializer.data) 
        return JsonResponse(group_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        group.delete() 
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def group_list_published(request):
    group = Groups.objects.filter(published=True)
        
    if request.method == 'GET': 
        group_serializer = GroupSerializer(group, many=True)
        return JsonResponse(group_serializer.data, safe=False)
    
