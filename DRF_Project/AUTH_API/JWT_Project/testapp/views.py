from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class EmployeeCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticated,]