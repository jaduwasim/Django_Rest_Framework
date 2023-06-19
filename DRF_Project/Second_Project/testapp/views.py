from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from .models import Employee
from .utils import is_json
from .mixins import HttpResponseMixins
from .serializers import EmployeeSerializer

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUD(HttpResponseMixins, View):

    def get_rsource_by_id(self, id):
        try:
            Query = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            Query = None
        return Query

    def post(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid :
            msg = {'msg':'Please Provide Data in JSON Foramt Only!'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string, status=400)
        stream = io.BytesIO(data)
        p_data = JSONParser().parse(stream)
        p_data_serialize = EmployeeSerializer(data=p_data)
        if p_data_serialize.is_valid():
            p_data_serialize.save()
            msg = {'msg':'Resource Created Success!'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string)
        json_string = JSONRenderer().render(p_data_serialize.errors)
        return self.render_to_http_response(json_string , status=400)
    
    def get(self, request , *args , **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            msg = {'msg':'Please Provide Data in JSON Foramt Only!'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string, status=400)
        stream = io.BytesIO(data)
        p_data = JSONParser().parse(stream)
        id = p_data.get('id',None)
        if id is not None:
            emp = self.get_rsource_by_id(id)
            if emp is None:
                msg = {'msg':'Record Note Available!'}
                json_string = JSONRenderer().render(msg)
                return self.render_to_http_response(json_string, status=404)
            empserialize = EmployeeSerializer(emp)
            json_string = JSONRenderer().render(empserialize.data)
            return self.render_to_http_response(json_string)
        emp = Employee.objects.all()
        empserialize = EmployeeSerializer(emp, many = True)
        json_string = JSONRenderer().render(empserialize.data)
        return self.render_to_http_response(json_string)
    
    def put(self, request , *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            msg = {'msg':'Please Provide Data in JSON Foramt Only!'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string, status=400)
        stream = io.BytesIO(data)
        p_data = JSONParser().parse(stream)
        id = p_data.get('id',None)
        if id is not None:
            emp = self.get_rsource_by_id(id)
            if emp is None:
                msg = {'msg':'Record is not Available!'}
                json_string = JSONRenderer().render(msg)
                return self.render_to_http_response(json_string, status=404)
            emp_seialize = EmployeeSerializer(emp, data=p_data, partial = True)
            if emp_seialize.is_valid():
                emp_seialize.save()
                msg = {'msg':'Record Updated!'}
                json_string = JSONRenderer().render(msg)
                return self.render_to_http_response(json_string)
            json_string = JSONRenderer().render(emp_seialize.errors)
            return self.render_to_http_response(json_string, status=400)
        msg = {'msg':'Reocrd not mathced found for Updation!'}
        json_string = JSONRenderer().render(msg)
        return self.render_to_http_response(json_string, status=400)

    def delete(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            msg = {'msg':'Please Provide Data in onlye JSON format!'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string, status=400)
        stream = io.BytesIO(data)
        p_data = JSONParser().parse(stream)
        id = p_data.get('id',None)
        if id is not  None:
            emp = self.get_rsource_by_id(id)
            if emp is None:
                msg = {'msg':'Record Matched not found!'}
                json_string = JSONRenderer().render(msg)
                return self.render_to_http_response(json_string, status=404)
            status, item = emp.delete()
            if status == 1 :
                msg = {'msg':'Record Deleted Succesfully!'}
                json_string = JSONRenderer().render(msg)
                return self.render_to_http_response(json_string)
            msg = {'msg':'Something goes wrong!! try after some time'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string, status=400)
        msg ={'msg':'id is missing, please provide!'}
        json_string = JSONRenderer().render(msg)
        return self.render_to_http_response(json_string, status=400)