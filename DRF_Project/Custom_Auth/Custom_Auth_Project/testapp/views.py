from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializers
from .authentication import CustomAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    authentication_classes = [CustomAuthentication,]
    permission_classes = [IsAuthenticated,]