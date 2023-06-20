from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.models import User
# Create your views here.

class EmployeeAPIView(APIView):
    def get(self, request, format=None):
        qs = Employee.objects.all()
        serialize = EmployeeSerializer(qs, many = True)
        return Response(serialize.data)
    
class EmployeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetriveAPIView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id' # Here lookup field bydefaul is pk, we are customizing here

class EmployeeUpdateAPIView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDestroyAPIView(DestroyAPIView):
    queryset = Employee
    serializer_class = EmployeeSerializer


class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetriveUpdateAPI(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetriveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'



# from rest_framework.generics import 
# ListAPIView, ----> for list out all resource
# CreateAPIView, ---> fro create a new rsource
# ListCreateAPIView, --> for list out all resource and  create a new resource 
# RetrieveAPIView ---> for get a particular resource 
# UpdateAPIView, ---> for update a resource
# DestroyAPIView, ---> for delete a resource
# RetrieveUpdateAPIView, --> for get a particular resource and Update that record
# RetrieveDestroyAPIView, ---> for get a particular resource and delete that record
# RetrieveUpdateDestroyAPIView ---> for get a paritcular resource and update that record and we can delete tha resource also 