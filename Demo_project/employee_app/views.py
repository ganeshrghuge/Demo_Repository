from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializer import EmployeeSerializer
from .models import Employee
# Create your views here.


class EmployeeAPI():
    def get(self):
        data = Employee.objects.all()
        serializer = EmployeeSerializer(data,many=True)
        return Response(serializer, data, status=200)
    def post(self,request,data):
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)
    def delete(self,request):
        pass
    def put(self,request):
        pass