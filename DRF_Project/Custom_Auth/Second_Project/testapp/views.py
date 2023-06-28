from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializers
from .authentication import CustomAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class EmployeeCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    authentication_classes = [CustomAuthentication,]
    permission_classes = [IsAuthenticated,]