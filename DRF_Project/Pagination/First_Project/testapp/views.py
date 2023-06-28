from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.pagination import PageNumberPagination
from .pagination import MyPagination
# Create your views here.

class EmployeeView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = MyPagination
