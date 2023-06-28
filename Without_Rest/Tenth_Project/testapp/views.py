from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from .mixins import HttpResponseMixins
from .form import EmployeeForm
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
# Create your views here.
from django.views.generic import View
from .utils import is_json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUD(HttpResponseMixins, View):
    def get_resource_by_id(id):
        try:
            Query = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            Query = None
        return Query
    
    def get(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            msg = {'msg':'Please Provide data in JSON Format!'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string, stauts=400)
        stream = io.BytesIO(data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id',None)
        if id is not None:
            emp = self.get_resource_by_id(id)
            if emp is None:
                msg = {'msg':'Resource Not Found!'}
                json_string = JSONRenderer().render(msg)
                return self.render_to_http_response(json_string, stauts=404)
            emp_serialize = EmployeeSerializer(emp)
            json_string = JSONRenderer().render(emp_serialize.data)
            return self.render_to_http_response(json_string)
        emp = Employee.objects.all()
        emp_serialize = EmployeeSerializer(emp, many=True)
        json_string = JSONRenderer().render(emp_serialize.data)
        return self.render_to_http_response(json_string)
    
    def post(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            msg = {'msg':'Please Provide data in JSON Format!'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string, stauts=400)
        stream = io.BytesIO(data)
        pdata = JSONParser().parse(stream)
        serialize = EmployeeSerializer(pdata)
        if serialize.is_valid():
            serialize.save()
            msg = {'msg':'Reocrd Created !'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string)
        json_string = JSONRenderer().render(serialize.errors)
        return self.render_to_http_response(json_string, stauts=400)
    
    def patch(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            msg = {'msg':'please insert data into json form only'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string, stauts=400)
        steam = io.BytesIO(data)
        pdata = JSONParser().parse(steam)
        id = pdata.get('id',None)
        if id is None:
            msg = {'msg':'Please provide id'}
            json_string = JSONRenderer().render(msg)
            return self.render_to_http_response(json_string, status=400)
        emp_obj = self.get_resource_by_id(id)
        if emp_obj is None:
            msg = {'msg':'Data is not available with your provided value!'}
            json_string = JSONParser().parse(msg)
            return self.render_to_http_response(json_string, status=400)
        old_data = {
            'eno' : emp_obj.eno,
            'ename':emp_obj.ename,
            'esal':emp_obj.esal,
            'eaddr':emp_obj.eaddr
        }
        old_data.update(pdata)
        form = EmployeeForm(old_data, instance = emp_obj)
        if form.is_valid():
            form.save(commit=True)
            msg = {'msg':'Updated Resource!'}
            json_string = JSONRenderer().render(msg)
            self.render_to_http_response(json_string,)
        json_string = JSONRenderer().render(form.errors)
        return self.render_to_http_response(json_string, stauts=400)
