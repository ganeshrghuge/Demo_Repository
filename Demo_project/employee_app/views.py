from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializer import EmployeeSerializer
from .models import Employee
from rest_framework.views import APIView
# Create your views here.


class EmployeeAPI(APIView):
    def get(self,request):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp,many=True)
        return Response(serializer.data, status=200)
    def post(self,request):
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)

class EmployeeDetailView(APIView):
    def get_object(self,id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist as e:
            return Response({"error":"not found"},status=400)

    def get(self,request,id=None):
        instance = self.get_object(id)
        serializer = EmployeeSerializer(instance)
        return Response(serializer.data)

    def put(self,request,id):
        data = request.data
        instance = self.get_object(id)
        serializer = EmployeeSerializer(instance,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors, status=400)

    def delete(self,request,id=None):
        instance = self.get_object(id)
        instance.delete()
        return Response(status=200)