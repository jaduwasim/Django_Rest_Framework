from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly, IsAuthenticatedOrReadOnly
from .permissions import CustomPermission
# Create your views here.
class EmployeeCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [CustomPermission,]
