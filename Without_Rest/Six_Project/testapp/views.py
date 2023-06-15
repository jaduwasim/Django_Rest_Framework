from django.shortcuts import render
from django.views.generic import View
from .models import Employee
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .mixins import SerializeMixins, HttpResponseMixin
import json
from .utils import is_json
from .form import EmployeeForm
# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeList(HttpResponseMixin, SerializeMixins, View):
    def get(self, request, *args, **kwargs):
        emp_list = Employee.objects.all()
        json_string = self.Serialize(emp_list)
        return self.render_to_http_response(json_string)
    
    def post(self, request, *args, **kwargs):
        provided_data = request.body
        print('provided data:',provided_data)
        valid = is_json(provided_data)
        if not valid:
            json_string = json.dumps({'msg':'Please Provide Data in json format !!!'})
            return self.render_to_http_response(json_string, status = 400)
        p_dict = json.loads(provided_data)
        form = EmployeeForm(p_dict)
        if form.is_valid():
            form.save(commit=True)
            json_string = json.dumps({'msg':'Resource Created Success !!!'})
            return self.render_to_http_response(json_string)
        if form.errors:
            json_string = json.dumps(form.errors)
            return self.render_to_http_response(json_string, status=400)
    
    

@method_decorator(csrf_exempt,name='dispatch')
class Employee_CBV(HttpResponseMixin, SerializeMixins, View):
    def get_object_id(self, id):
        try:
            Query = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            Query = None
        return Query

    def get(self,request, id , *args, **kwargs):
        emp_obj = self.get_object_id(id)
        if emp_obj is None:
            json_string = json.dumps({'msg':'Records is not Found!'})
            return self.render_to_http_response(json_string)
        json_string = self.Serialize([emp_obj,])
        return self.render_to_http_response(json_string)
    
        
    def put(self, request, id, *args, **kwargs):
        emp_obje = self.get_object_id(id)
        if emp_obje is None:
            json_string = json.dumps({'msg':'Record not Found!!!'})
            return self.render_to_http_response(json_string, status=404)
        provided_data = request.body
        valid = is_json(provided_data)
        if not valid:
            json_string = json.dumps({'msg':'please proved data in json format!!!'})
            return self.render_to_http_response(json_string, status=400)
        p_dict = json.loads(provided_data)
        old_data = {
            'eno': emp_obje.eno,
            'ename':emp_obje.ename,
            'esal':emp_obje.esal,
            'eaddr':emp_obje.eaddr
        }
        old_data.update(p_dict)
        form = EmployeeForm(old_data, instance=emp_obje)
        if form.is_valid():
            form.save(commit=True)
            json_string = json.dumps({'msg':'Resorces Updated Success'})
            return self.render_to_http_response(json_string)
        if form.errors:
            json_string = json.dumps({'msg':'Please try again after sometimes'})
            return self.render_to_http_response(json_string, status=400)

    def delete(self, request, id , *args, **kwargs):
        emp_obj = self.get_object_id(id)
        if emp_obj is None:
            json_string = json.dumps({'msg':'Record Not found!!!'})
            return self.render_to_http_response(json_string, status=404)
        status, item_object = emp_obj.delete()
        if status == 1:
            json_string = json.dumps({'msg':'Data Deleted'})
            return self.render_to_http_response(json_string)
        json_string = json.dumps({'msg':'Something goes wrong, please try again'})
        return self.render_to_http_response(json_string, status=400)