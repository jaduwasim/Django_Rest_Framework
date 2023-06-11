from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
import json
from django.http import HttpResponse
from django.core.serializers import serialize
from testapp.mixins import SerializeMixin
# Create your views here.
class EmployeeDetaliCBV(View):
    def get(self, request,id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'The requested resource not Available'})
            return HttpResponse(json_data, content_type='application/json', status=404)
        else:
            emp_data={
                'eno':emp.eno,
                'ename':emp.ename,
                'esal':emp.esal,
                'eaddr':emp.eaddr,
            }
            json_data = json.dumps(emp_data)
        return HttpResponse(json_data, content_type='application/json',status=200)

# using django json concepts
class EmployeeDetaliCBV2(View):
    def get(self, request,id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'The requested resource not Available'})
            return HttpResponse(json_data, content_type='application/json', status=404)
        else:
            json_data = serialize('json', [emp,], fields=('eno','ename'))
        return HttpResponse(json_data, content_type='application/json', status=200)


# using mixins concepts:
class EmployeeDetaliMixinCBV2(SerializeMixin, View):
    def get(self, request,id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'The requested resource not Available'})
            return HttpResponse(json_data, content_type='application/json', status=404)
        else:
            json_data = self.serialize([emp,])
        return HttpResponse(json_data, content_type='application/json',status=200)


# using mixins concepts(using python concepts)
class EmployeeListCBV2(View):
    def get(self, request, *args, **kwargs):
        emp = Employee.objects.all()
        # json_data = serialize('json', emp, fields = ('eno','ename','eaddr'))
        json_data = serialize('json', emp)
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            emp_data = obj['fields']
            final_list.append(emp_data)
        json_data = json.dumps(final_list)
        return HttpResponse(json_data, content_type='application/json')

# using mixins concepts:
class EmployeeMixinCBV2(SerializeMixin ,View):
    def get(self, request, *args, **kwargs):
        emp = Employee.objects.all()
        json_data = self.serialize(emp)
        return HttpResponse(json_data, content_type='application/json')
