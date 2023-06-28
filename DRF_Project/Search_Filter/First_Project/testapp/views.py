from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

# Create your views here.

class EmployeeCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    # search_fields = ('ename','eno',) #contains data
    # search_fields = ('=eno',) #Exact Match
    # search_fields = ('^eno',) #Start With
    ordering_fields = ('eno','esal')
    
class EmployeeListAPI(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    # ordering_fields=['eno','esal']

