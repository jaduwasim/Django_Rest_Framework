from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerialziers
from .pagination import MyLimitOffsetPagination, MyCursorPagination
from rest_framework.pagination import LimitOffsetPagination 
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class EmployeeCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerialziers
    pagination_class = MyCursorPagination