from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from .models import Employee
from .serializers import EmployeeSerializer
from .utils import is_json
from .mixins import HttpResponseMixins

# Create your views here.

@method_decorator(csrf_exempt, name= 'dispatch')
class EmployeeCRUD(HttpResponseMixins , View):
    def get_rsource_by_id(self, id):
        try:
            Query = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            Query =  None
        
        return Query

    def post(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            msg = {'msg':'Please Provide Data in JSON'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string, status=400)
        stream = io.BytesIO(data)
        pdata = JSONParser().parse(stream)
        serialize = EmployeeSerializer(data=pdata)
        if serialize.is_valid():
            serialize.save()
            msg = {'msg':'Record Created !'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string)
        json_string = JSONRenderer().render(serialize.errors)
        return self.render_to_http_response(json_string, status=400)
    
    def get(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            msg = {'msg':'Please Provide Data in JSON form Only!'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string, status=400)
        stream = io.BytesIO(data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id',None)
        if id is not None:
            emp = self.get_rsource_by_id(id)
            if emp is None:
                msg = {'msg':'Record not matched not found !'}
                json_string = JSONRenderer().render(msg)
                return self.render_to_http_response(json_string, status=400)
            empserialize = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(empserialize.data)
            return self.render_to_http_response(json_data)
        emp = Employee.objects.all()
        empserialize = EmployeeSerializer(emp, many=True)
        json_data = JSONRenderer().render(empserialize.data)
        return self.render_to_http_response(json_data)

    def put(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            msg = {'msg':'Please Enter Data in JSON Format Onlye'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string, status=400)
        stream = io.BytesIO(data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id', None)
        if id is not None:
            emp = self.get_rsource_by_id(id)
            if emp is None:
                msg = {'msg':'Data not found!'}
                json_string = JSONRenderer().render(msg)
                return self.render_to_http_response(json_string, status=404)
            serialize = EmployeeSerializer(emp, data=pdata, partial = True)
            if serialize.is_valid():
                serialize.save()
                msg = {'msg':'Record Updated Success!'}
                json_string = JSONRenderer().render(msg)
                return self.render_to_http_response(json_string)
            json_string = JSONRenderer().render(serialize.errors)
            return self.render_to_http_response(json_string, status=400)
        msg = {'msg':'please provide id'}
        json_string = JSONRenderer().render(msg)
        return self.render_to_http_response(json_string , status=400)
    
    def delete(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            msg = {'msg':'Please Enter Data in JSON Format Onlye'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string, status=400)
        stream = io.BytesIO(data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id',None)
        if id is not None:
            emp = self.get_rsource_by_id(id)
            if emp is None:
                msg = {'msg':'Data not found!'}
                json_string = JSONRenderer().render(msg)
                return self.render_to_http_response(json_string, status=404)
            status, item = emp.delete()
            if status == 1 :
                msg = {'msg':'Record has Deleted!'}
                json_string = JSONRenderer().render(msg)
                return self.render_to_http_response(json_string)
        msg = {'msg':'please provide id'}
        json_string = JSONRenderer().render(msg)
        return self.render_to_http_response(json_string , status=400)