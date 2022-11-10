from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from family.models import Family
from family.serializers import FamilySerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def family_list(request):
    if request.method == 'GET':
        family = Family.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            family = family.filter(title__icontains=title)
        
        family_serializer = FamilySerializer(family, many=True)
        return JsonResponse(family_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        family_data = JSONParser().parse(request)
        family_serializer = FamilySerializer(data=family_data)
        if family_serializer.is_valid():
            family_serializer.save()
            return JsonResponse(family_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(family_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Family.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def family_detail(request, pk):
    try: 
        family = Family.objects.get(pk=pk) 
    except Family.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        family_serializer = FamilySerializer(family) 
        return JsonResponse(family_serializer.data) 
 
    elif request.method == 'PUT': 
        family_data = JSONParser().parse(request) 
        family_serializer = FamilySerializer(family, data=family_data) 
        if family_serializer.is_valid(): 
            family_serializer.save() 
            return JsonResponse(family_serializer.data) 
        return JsonResponse(family_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        family.delete() 
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def family_list_published(request):
    family = Family.objects.filter(published=True)
        
    if request.method == 'GET': 
        family_serializer = FamilySerializer(family, many=True)
        return JsonResponse(family_serializer.data, safe=False)
    
