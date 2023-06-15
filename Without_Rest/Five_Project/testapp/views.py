from django.shortcuts import render
from django.views.generic import View
from .models import Employee
import json
from .mixins import SerializeMixin, HttpResponseMixins
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import Employee_Form
from .utils import is_json
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class Employee_List_CBV(HttpResponseMixins, SerializeMixin, View):

    def get_resource_by_id(self, id):
        try:
            Query = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            Query = None
        return Query

    def get(self, request, id, *args, **kwargs):
        emp_data = self.get_resource_by_id(id)
        if emp_data is None:
            json_string = json.dumps({'msg':'Data not Found!!!'})
            return self.render_to_http_response(json_string, status = 404)
        json_string = self.serialize([emp_data,])
        return self.render_to_http_response(json_string)
    
    def put(self, request, id,  *args, **kwargs):
        emp_data = self.get_resource_by_id(id)
        print(f'emp data : {emp_data}')
        if emp_data is None:
            json_string = json.dumps({'msg':'Records not mathded Found!!!'})
            return self.render_to_http_response(json_string)
        json_string = request.body
        print(f'json string : {json_string}')
        valid_json = is_json(json_string)
        if not valid_json:
            json_string = json.dumps({'msg':'Please Enter Valid Json!!!'})
            return self.render_to_http_response(json_string)
        provided_dict = json.loads(json_string)
        original_dict = {
            'eno':emp_data.eno,
            'ename':emp_data.ename,
            'esal':emp_data.esal,
            'eaddr':emp_data.eaddr
        }
        original_dict.update(provided_dict)
        form = Employee_Form(original_dict, instance=emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_string = json.dumps({'msg':'Resource Created'})
            return self.render_to_http_response(json_string)
        if form.errors:
            json_string = json.dumps(form.errors)
            return self.render_to_http_response(json_string, status=500)
        
    def delete(self, request, id, *args, **kwargs):
        emp_data = self.get_resource_by_id(id)
        if emp_data is None:
            json_string = json.dumps({'msg':'Recourse is not Available!!'})
            return self.render_to_http_response(json_string, status=404)
        status, delted_item =emp_data.delete()
        if status == 1:
            json_string = json.dumps({'msg':'Recourse Deleted'})
            return self.render_to_http_response(json_string)
        else:
            json_string = json.dumps({'msg':'please try again'})
            return self.render_to_http_response(json_string)        
    

class EmployeeCBV(HttpResponseMixins, SerializeMixin, View):
    def get(self, request, *args, **kwargs):
        emp_list = Employee.objects.all()
        json_string = self.serialize(emp_list)
        # return HttpResponse(json_string, content_type = 'application/json')
        return self.render_to_http_response(json_string)
        