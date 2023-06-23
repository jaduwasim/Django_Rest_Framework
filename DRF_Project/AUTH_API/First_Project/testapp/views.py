from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerialzier
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class EmployeeCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerialzier
    authentication_classes = [TokenAuthentication,]
    permission_classes = [DjangoModelPermissions,]