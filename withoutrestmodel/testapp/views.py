from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
import json
from django.http import HttpResponse
from django.core.serializers import serialize
# Create your views here.
class EmployeeDetaliCBV(View):
    def get(self, request,id, *args, **kwargs):
        emp = Employee.objects.get(id=id)
        emp_data={
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr,
        }
        json_data = json.dumps(emp_data)
        return HttpResponse(json_data, content_type='application/json')

class EmployeeDetaliCBV2(View):
    def get(self, request,id, *args, **kwargs):
        emp = Employee.objects.get(id=id)
        json_data = serialize('json', [emp,], fields=('eno','ename'))
        return HttpResponse(json_data, content_type='application/json')

