from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListAPIView, RetrieveAPIView
# Create your views here.

class EmployeeRetrives(CreateModelMixin, ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class EmployeeDetailAPIView(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args, **kwargs)