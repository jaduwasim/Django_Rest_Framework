from django.shortcuts import render
from .models import Employee
from django.views.generic import View
import json
from django.http import HttpResponse
from django.core.serializers import serialize
from .mixins import SerializeMixin, HttpResponseMixin
# Create your views here.

class EmployeeCBV(HttpResponseMixin, SerializeMixin, View):
    def get(self, request, id , *args, **kwargs):
        # try:
        #     emp = Employee.objects.get(id=id)
        #     emp_dict = {
        #         'eno':emp.eno,
        #         'ename':emp.ename,
        #         'esal':emp.esal,
        #         'eaddr':emp.eaddr
        #     }
        #     json_string = json.dumps(emp_dict)
        #     return HttpResponse(json_string)
        # except:
        #     return HttpResponse('Data is not Available')


        # By serialize Module:
        # we shuold import the module from
        # from django.core.serializer import serialize
        # emp_json = serialize('json',[emp], fields = ('ename', 'eaddr')) #for finding particular fields

        # emp = Employee.objects.get(id=id)
        # emp_json = self.serialize([emp,])
        # return HttpResponse(emp_json)

        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_string = json.dumps({'msg':'The Requested Rsource is not available'})
            # return HttpResponse(json_string, content_type = 'application/json')
            return self.render_to_http_response(json_string, status=404)
        else:
            emp_json = self.serialize([emp,])
            # return HttpResponse(emp_json, content_type = 'application/json', status = 200)
            return self.render_to_http_response(emp_json)

class Emploee_List_CBV(SerializeMixin, View):
    def get(self, request, *args, **kwargs):
        emp_list = Employee.objects.all()
        json_emp = self.serialize(emp_list)
        return HttpResponse(json_emp, content_type = 'application/json', status=200)