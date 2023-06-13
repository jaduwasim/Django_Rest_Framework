from django.shortcuts import render
from django.views.generic import View
from .models import Employee
import json
from django.http import HttpResponse
from django.core.serializers import serialize
from .mixins import SerializeMixins, HttpResponseMixin

# Create your views here.

class EmployeCBV(HttpResponseMixin, SerializeMixins, View):
    def get(self, request,id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'The Request Resource is not available'})
            return self.render_to_http_response(json_data, status = 404)
        else:
            emp_json = self.Serialize([emp,])
            return self.render_to_http_response(emp_json)

class EmployeeListCBV(HttpResponseMixin, SerializeMixins,View):
    def get(self, request, *args, **kwargs):
        emp_list = Employee.objects.all()
        emp_json = self.Serialize(emp_list)
        return self.render_to_http_response(emp_json)