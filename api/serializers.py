from rest_framework import serializers
from accounts.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ("id", "username", "email", "password", "uid")

    
    def create(self, validated_data):
        password = validated_data.pop("password")
        employee = Employee.objects.create(**validated_data)
        employee.set_password(password)
        employee.save()
        return employee
