from django.shortcuts import render
from .models import Employee
from django.views.generic import View
import json
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from .mixins import SerializeMixins, HttpResponseMixins
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .form import EmployeeForm
from .utils import is_json

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCBV(HttpResponseMixins, SerializeMixins,View):

    def get_resorce_by_id(self,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def get(self, request,id, *args, **kwargs):
        emp_obj = self.get_resorce_by_id(id)
        if emp_obj is None:
            msg = {'msg':'Record not Found!'}
            json_string = json.dumps(msg)
            return self.render_to_http_response(json_string, status=400)
        json_string = self.serialize([emp_obj,])
        return self.render_to_http_response(json_string)

    def put(self, request,id, *args, **kwargs):
        emp_obj = self.get_resorce_by_id(id)
        if emp_obj is None:
            json_string = json.dumps({'msg':'Reocrd Not Found!'})
            return self.render_to_http_response(json_string, status=400)
        data = request.body
        valid = is_json(data)
        if not valid:
            json_string = json.dumps({'msg':'Please Send Data into JSON Format Only!'})
            return self.render_to_http_response(json_string, status=400)
        new_data = json.loads(data)
        old_data = {
            'eno':emp_obj.eno,
            'ename':emp_obj.ename,
            'esal':emp_obj.esal,
            'eaddr':emp_obj.eaddr
        }
        old_data.update(new_data)
        print(f'Old Data: {old_data}')
        form = EmployeeForm(old_data, instance=emp_obj)
        if form.is_valid():
            form.save(commit=True)
            json_string = json.dumps({'msg':'Record Updated Successfully!'})
            return self.render_to_http_response(json_string)
        json_string = json.dumps(form.errors)
        return self.render_to_http_response(json_string, status=400)
    
    def delete(self, request, id, *args, **kwargs):
        emp_obj = self.get_resorce_by_id(id)
        if emp_obj is None:
            json_string = json.dumps({'msg':'Reocrd Not Matched Found!'})
            return self.render_to_http_response(json_string, status=400)
        status, del_item = emp_obj.delete()
        if status == 1:
            json_string = json.dumps({'msg':'Reocrd Deleted Success!'})
            return self.render_to_http_response(json_string, status=400)            
        json_string = json.dumps({'msg':'Something gone wrong!'})
        return self.render_to_http_response(json_string, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class EmplyeeGetCreateView(SerializeMixins, HttpResponseMixins,View):

    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        pdata = self.serialize(qs)
        json_string = json.dumps(pdata)
        return self.render_to_http_response(json_string)

    def post(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            json_string = json.dumps({'msg':'Please Send Data into JSON Format Only!'})
            return self.render_to_http_response(json_string, status=400)
        pdata = json.loads(data)
        form = EmployeeForm(pdata)
        if form.is_valid():
            form.save(commit=True)
            json_string = json.dumps({'msg':'Record Created Success!'})
            return self.render_to_http_response(json_string, status=400)
        json_string = json.dumps({form.errors})
        return self.render_to_http_response(json_string, status=400)
        
