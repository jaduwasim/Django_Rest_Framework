from testapp.models import Employee
from .serializers import EmployeeSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class  EmployeeCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)