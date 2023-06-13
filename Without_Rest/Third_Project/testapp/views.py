from django.shortcuts import render
from django.views.generic import View
from .models import Employee
import json
from django.http import HttpResponse

# Create your views here.
class EmployeeCBV(View):
    def get(self, request, id, *args, **kwargs):
        emp = Employee.objects.get(id=id)
        emp_dict = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr
        }
        emp_json = json.dumps(emp_dict)
        return HttpResponse(emp_json)