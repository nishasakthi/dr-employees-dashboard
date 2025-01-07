from django.shortcuts import render
from .models import Hundred
from .serializers import HundredSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

def index(request):
    return render(request, 'index.html')

@api_view(['GET', 'POST'])
def employees_list(request):
    if request.method == 'POST':
        serializer = HundredSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        employees = Hundred.objects.all()
        serializer = HundredSerializer(employees, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):

    try:
        employee = Hundred.objects.get(pk=pk)
    except Hundred.DoesNotExist:
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HundredSerializer(employee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = HundredSerializer(instance=employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


