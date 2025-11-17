from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from accounts.models import Employee
from .serializers import EmployeeSerializer


class EmployeeAPIView(APIView):

    def get(self, request):
        """Список сотрудников"""
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailView(APIView):
    def get(self, request, uid):
        """Получить сотрудника по uid"""
        employee = get_object_or_404(Employee, uid=uid)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, uid):
        """Полное обновление сотрудника"""
        employee = get_object_or_404(Employee, uid=uid)
        serializer = EmployeeSerializer(employee, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, uid):
        """Частичное обновление сотрудника"""
        employee = get_object_or_404(Employee, uid=uid)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

