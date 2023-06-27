from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializers import EmployeeSerializers

# Create your views here.

class EmployeeCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated,]