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
        return Response(serializer,status=200)
    def post(self,request):
        pass
    def delete(self,request):
        pass
    def put(self,request):
        pass