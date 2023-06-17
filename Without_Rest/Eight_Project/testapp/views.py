from django.shortcuts import render
from django.views.generic import View
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .mixins import SerializeMixins, HttpResponseMixins
from .utils import is_json
import json
from .form import EmployeeForm

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class EmployeerCRUD(HttpResponseMixins, SerializeMixins, View):

    def get_resource_by_id(self, id):
        try:
            Query = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            Query = None

        return Query

    def get(self,request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            json_string = json.dumps({'msg':'Please Enter only json data'})
            return self.render_to_http_response(json_string,status=400)
        p_dict = json.loads(data)
        id = p_dict.get('id', None)
        if id is not None:
            emp = self.get_resource_by_id(id)
            if emp is None:
                json_string = json.dumps({'msg':'Record not mathced found!!!'})
                return self.render_to_http_response(json_string, status=404)
            emp_data = self.serialize([emp,])
            return self.render_to_http_response(emp_data)
        
        emp_list = Employee.objects.all()
        emp_json = self.serialize(emp_list)
        return self.render_to_http_response(emp_json)


    def post(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            json_string = json.dumps({'msg':'Please Enter Data in only in json'})
            return self.render_to_http_response(json_string, status=400)
        p_dict = json.loads(data)
        form = EmployeeForm(p_dict)
        if form.is_valid():
            form.save(commit=True)
            json_string = json.dumps({'msg':'Record Created Success!'})
            return self.render_to_http_response(json_string)
        if form.errors:
            json_string = json.dumps(form.errors)
            return self.render_to_http_response(json_string, status=400)
    
    def put(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            json_string = json.dumps({'msg':'Please Enter Data in only in json'})
            return self.render_to_http_response(json_string, status=400)
        new_data = json.loads(data)
        id = new_data.get('id', None)
        emp_obj = self.get_resource_by_id(id)
        if emp_obj is None:
            json_string = json.dumps({'msg':'Data not matched found, Can not update'})
            return self.render_to_http_response(json_string,status=400)
        old_data = {
            'eno':emp_obj.eno,
            'ename':emp_obj.ename,
            'esal':emp_obj.esal,
            'eaddr':emp_obj.eaddr
        }
        old_data.update(new_data)
        form = EmployeeForm(old_data, instance=emp_obj)
        if form.is_valid():
            form.save(commit=True)
            json_string = json.dumps({'msg':'Record Update Success!'})
            return self.render_to_http_response(json_string)

        if form.errors:
            json_string =json.dumps(form.errors)
            return self.render_to_http_response(json_string, status=400)
    
    def delete(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            json_string = json.dumps({'msg':'Please Enter Data in only in json'})
            return self.render_to_http_response(json_string, status=400)
        p_dict = json.loads(data)
        id = p_dict.get('id',None)
        emp_obje = self.get_resource_by_id(id)
        if emp_obje is None:
            json_string = json.dumps({'msg':'Record Not Matched Found!'})
            return self.render_to_http_response(json_string, status=404)
        status, item_obj = emp_obje.delete()
        if status == 1:
            json_string = json.dumps({'msg':'Record Deleted!'})
            return self.render_to_http_response(json_string)
        
        json_string = json.dumps({'msg':'Try again after some times'})
        return self.render_to_http_response(json_string, status=400)
