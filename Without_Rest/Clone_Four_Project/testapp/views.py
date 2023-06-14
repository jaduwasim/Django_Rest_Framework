from django.shortcuts import render
from django.views.generic import View
from .models import Employee
import json
from django.http import HttpResponse
from django.core.serializers import serialize
from .mixins import SerializeMixins, HttpResponseMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from testapp.utils import is_json
from testapp.form import EmployeeForm
# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class EmployeCBV(HttpResponseMixin, SerializeMixins, View):
    def get_resource_by_id(self, id):
        try:
            Query = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            Query = None
        return Query
    def get(self, request,id, *args, **kwargs):       
        emp = self.get_resource_by_id(id)
        if emp is None:
            emp_json = json.dumps({'msg':'The Resources Not Found!!!'})
            return self.render_to_http_response(emp_json, status=404)
        emp_json = self.Serialize([emp,])
        return self.render_to_http_response(emp_json)

    def put(self,request, id, *args, **kwargs):
        emp_data = self.get_resource_by_id(id=id)
        if emp_data is None:
            json_string = json.dumps({'msg':'Matched Resources not found!!!! we can perform this operation'})
            return self.render_to_http_response(json_string)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_string = json.dumps({'msg':'Please Enter valid json'})
            return self.render_to_http_response(json_string, status=400)
        emp_dict = json.loads(data)
        print(f'Employee Dictionary: {emp_dict}')
        original_dict = {
            'eno' : emp_data.eno,
            'ename':emp_data.ename,
            'esal': emp_data.esal,
            'eaddr':emp_data.eaddr
        }
        print(f'Original dict before updation: {original_dict}')
        original_dict.update(emp_dict)
        print(f'Original Dictionary After Update: {original_dict}')
        form = EmployeeForm(original_dict, instance=emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_string = json.dumps({'msg': 'Recources Update Success'})
            return self.render_to_http_response(json_string)
        if form.errors:
            json_string = json.dumps(form.errors)
            return self.render_to_http_response(json_string)
        
    def delete(self, request , id , *args, **kwargs):
        emp_data = self.get_resource_by_id(id)
        if emp_data is None:
            json_string = json.dumps({'msg':'Record Not found!!!'})
            return self.render_to_http_response(json_string, status=404)
        status, deleted_item = emp_data.delete()
        print(f'deleted_item {deleted_item}')
        if status == 1:
            json_string =json.dumps({'msg':'data deleted'})
            return self.render_to_http_response(json_string)
        json_string = json.dumps({'msg':'Unable to process, please try again!!!'})
        return self.render_to_http_response(json_string, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCBV(HttpResponseMixin, SerializeMixins,View):
    def get(self, request, *args, **kwargs):
        emp_list = Employee.objects.all()
        emp_json = self.Serialize(emp_list)
        return self.render_to_http_response(emp_json)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        if not is_json(json_data):
            json_string = json.dumps({'msg':'Please Enter Data in json format only'})
            return self.render_to_http_response(json_string, status=400)
        # json_string = json.dumps({'msg':'You Entred Data in Json format'})
        # return self.render_to_http_response(json_string)
        emp_dict = json.loads(request.body)
        form = EmployeeForm(emp_dict)
        if form.is_valid():
            obj = form.save(commit=True)
            json_string = json.dumps({'msg':'Resource Created Succesfull'})
            return self.render_to_http_response(json_string)
        if form.errors:
            json_string = json.dumps(form.errors)
            return self.render_to_http_response(json_string, status=400)