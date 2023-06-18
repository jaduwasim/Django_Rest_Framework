from django.shortcuts import render
from django.views.generic import View
from .models import Employee
from .serializers import EmployeeSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .utils import is_json
from .mixins import HttpResponseMixins
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name= 'dispatch')
class EmployeeCRUD(HttpResponseMixins, View):

    def get_resoure_by_id(self, id):
        try:
            Query = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            Query = None
        return Query

    def get(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            json_string = JSONRenderer().render({'msg':'Data shold be in JSON Form only'})
            return self.render_to_http_response(json_string, status=400)
        stream = io.BytesIO(data)
        p_dict = JSONParser().parse(stream)
        id = p_dict.get('id', None)
        if id is not None:
            emp = self.get_resoure_by_id(id)
            if emp is None:
                json_string = JSONRenderer().render({'msg':'Record not Matched Found!'})
                return self.render_to_http_response(json_string, status=404)
            empserialize = EmployeeSerializer(emp)
            emp_json = JSONRenderer().render(empserialize.data)
            return self.render_to_http_response(emp_json)
        emp = Employee.objects.all()
        empserialize = EmployeeSerializer(emp, many= True)
        emp_json = JSONRenderer().render(empserialize.data)
        return self.render_to_http_response(emp_json)
            
    def post(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            msg = {'msg':'Data should be JSON Form only!'}
            json_string =  JSONRenderer().render(msg)
            return self.render_to_http_response(json_string, status=400)
        stream = io.BytesIO(data)
        p_dict = JSONParser().parse(stream)
        new_data = EmployeeSerializer(data=p_dict) #data = new_data, Here data keyword is mandatory 
        if new_data.is_valid():
            new_data.save()
            msg = {'msg':'Record Created !'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string)
        json_string = JSONRenderer().render(new_data.errors)
        return self.render_to_http_response(json_string, status=400)
    
    def put(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            msg = {'msg':'Only JSON Formated Data should Accepts!'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string, status=400)
        stram = io.BytesIO(data)
        new_data = JSONParser().parse(stram)
        id = new_data.get('id', None)
        if id is not None:
            emp_data = self.get_resoure_by_id(id)
            if emp_data is None:
                msg = {'msg':'Record not Found!'}
                json_string = JSONRenderer().render(msg)
                return self.render_to_http_response(json_string, status=404)
            serialize = EmployeeSerializer(emp_data, data=new_data, partial = True)
            if serialize.is_valid():
                serialize.save()
                msg = {'msg':'Record Updated!'}
                json_string = JSONRenderer().render(msg)
                return self.render_to_http_response(json_string, status=404)
            json_string = JSONRenderer().render(serialize.errors)
            return self.render_to_http_response(json_string, status=404)
        
        msg = {'msg':'Please provide id'}
        json_string = JSONRenderer().render(msg)
        return self.render_to_http_response(json_string, status=404)
    
    def delete(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            msg = {'msg':'Only JSON Formated Data should Accepts!'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string, status=400)
        stream = io.BytesIO(data)
        p_data = JSONParser().parse(stream)
        id = p_data.get('id', None)
        if id is not None:
            emp = self.get_resoure_by_id(id)
            if emp is None:
                msg = {'msg':'Record Not Matched Found!'}
                json_string = JSONRenderer().render(msg)
                return self.render_to_http_response(json_string, status=404)
            status, item = emp.delete()
            if status == 1 :
                msg = {'msg':'Data Deleted!'}
                json_string = JSONRenderer().render(msg)
                return self.render_to_http_response(json_string)

            msg = {'msg':'something goes wrong! try after sometimes'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string)
        msg = {'msg':'Please Provide Id'}
        json_string = JSONRenderer().render(msg)
        return self.render_to_http_response(json_string)
            
        
