from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *

try:
    from ..members.models import User
except:
    from members.models import User



@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def employee_details(request):

    if request.method == "GET":
        employee = Employee_details.objects.filter(owner=request.user)
        serializer = EmployeeSerializer(employee,many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET','PUT','DELETE'])
def employee_list(request,id):
    try:
        employee = Employee_details.objects.all()
        obj = get_object_or_404(employee, id=id)
    except:
        return Response({'error': 'Doesn\'t Exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = EmployeeSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


    elif request.method == "PUT":
        employee = Employee_details.objects.all()
        obj = get_object_or_404(employee, id=id)
        serializer_class = EmployeeSerializer
        data = serializer_class(instance=obj, data=request.data)
        if data.is_valid(raise_exception=True):
            data.save()
            return Response(data.data, status=status.HTTP_200_OK)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee = Employee_details.objects.all()
        obj = get_object_or_404(employee, id=id)
        if obj:
            obj.delete()
            return Response({'message':'Deleted'},status=status.HTTP_200_OK)
    return Response({'error':'Not found'},status=status.HTTP_404_NOT_FOUND)

