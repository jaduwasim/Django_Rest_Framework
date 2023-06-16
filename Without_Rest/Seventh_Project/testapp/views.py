from django.shortcuts import render
from django.views.generic import View
from .models import Employee
from .mixins import SerializationMixins, HttpResponseMixin
from .utils import is_json
import json
from .form import EmployeeForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class Employee_list(HttpResponseMixin, SerializationMixins, View):
    def get(self, request, *args, **kwargs):
        emp_list = Employee.objects.all()
        json_string = self.serialization(emp_list)
        return self.render_to_http_response(json_string)
    
    def post(self, request, *args, **kwargs):
        data= request.body
        valid = is_json(data)
        if not valid:
            json_string = json.dumps({'msg':'Please Enter data in JSON formata only !!!'})
            return self.render_to_http_response(json_string, status=400)
        p_dict = json.loads(data)
        form = EmployeeForm(p_dict)
        if form.is_valid():
            form.save(commit=True)
            json_string = json.dumps({'msg':'Resource Created Success!!!'})
            return self.render_to_http_response(json_string)
        if form.errors:
            json_sting = json.dumps(form.errors)
            return self.render_to_http_response(json_sting, status=400)
    
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCBV(HttpResponseMixin, SerializationMixins, View):

    def get_record_by_id(self, id):
        try:
            Query = Employee.objects.get(id=id)
        except:
            Query = None
        return Query

    def get(self, request, id , *args, **kwargs):
        emp_data = self.get_record_by_id(id)
        if emp_data is None:
            json_string = json.dumps({'msg':'Reocrd not Matched Found!!'})
            return self.render_to_http_response(json_string, status=404)
        json_data = self.serialization([emp_data,])
        return self.render_to_http_response(json_data)
    
    def put(self, request, id, *args, **kwargs):
        emp_data = self.get_record_by_id(id)
        if emp_data is None:
            json_string = json.dumps({'msg':'Reocrd not Matched Found!!'})
            return self.render_to_http_response(json_string, status=404)
        data = request.body
        valid = is_json(data)
        if not valid:
            json_string = json.dumps({'msg':'Please Enter data in JSON formata only !!!'})
            return self.render_to_http_response(json_string, status=400)
        new_data = json.loads(data)
        print('new data:',new_data)
        old_data = {
            'eno':emp_data.eno,
            'ename':emp_data.ename,
            'esal':emp_data.esal,
            'eaddr':emp_data.eaddr
        }
        old_data.update(new_data)
        print('old data:', old_data)
        form = EmployeeForm(old_data, instance=emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_string = json.dumps({'msg':'Record Updated'})
            return self.render_to_http_response(json_string)
        if form.errors:
            json_string = json.dumps({'msg':'Please try again after some times'})
            return self.render_to_http_response(json_string, status=400)

    def delete(self, request, id , *args, **kwargs):
        emp_data = self.get_record_by_id(id)
        if emp_data is None:
            json_string = json.dumps({'msg':'Reocrd not Matched Found!!'})
            return self.render_to_http_response(json_string, status=404)

        status, delte_item = emp_data.delete()
        if status == 1:
            json_string = json.dumps({'msg':'Record Deleted'})
            return self.render_to_http_response(json_string)
        json_string = json.dumps({'msg':'Please try again, after some time'})
        return self.render_to_http_response(json_string, status=400)

        