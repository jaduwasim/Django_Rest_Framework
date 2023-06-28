from rest_framework import serializers
from .models import Employee

class EmployeeSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'