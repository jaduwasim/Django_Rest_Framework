from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from .utils import is_json
import json
from .mixins import SerializationMixins, HttpResponseMxins
from .form import StudentForm
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class StudentCRUD(HttpResponseMxins, SerializationMixins,View):
    def get_reosurce_by_id(self,id):
        try:
            Query = Student.objects.get(id=id)
        except Student.DoesNotExist:
            Query = None

        return Query
    
    def get(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            json_string = json.dumps({'msg':'Please Enter Data in only JSON Format'})
            return self.render_to_http_response(json_string, status=400)
        p_dict = json.loads(data)
        id = p_dict.get('id',None)
        if id is not None:
            std_obj = self.get_reosurce_by_id(id)
            if std_obj is None:
                json_string = json.dumps({'msg':'Record not Matched found!'})
                return self.render_to_http_response(json_string, status=404)
            std_json = self.serialization([std_obj])
            return self.render_to_http_response(std_json)
        std_list = Student.objects.all()
        std_list_json = self.serialization(std_list)
        return self.render_to_http_response(std_list_json)
    
    def post(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if  not valid :
            json_string = json.dumps({'msg':'Please Enter Data in only JSON Format'})
            return self.render_to_http_response(json_string, status= 400)
        p_dict = json.loads(data)
        form = StudentForm(p_dict)
        if form.is_valid():
            form.save()
            json_string = json.dumps({'msg':'Record Created!'})
            return self.render_to_http_response(json_string)
        if form.errors: 
            json_string = json.dumps(form.errors)
            return self.render_to_http_response(json_string, status=400)
    
    def put(self, request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            json_string = json.dumps({'msg':'Please Enter Data in only JSON Format'})
            return self.render_to_http_response(json_string, status= 400)
        new_data = json.loads(data)
        id = new_data.get('id',None)
        if id is None:
            json_string = json.dumps({'msg':' for updation, id is Mandatory!'})
            return self.render_to_http_response(json_string, status=400)
        std_obj = self.get_reosurce_by_id(id)
        if std_obj is None:
            json_string = json.dumps({'msg':'Record not Found with given id'})
            return self.render_to_http_response(json_string, status=404)
        old_data = {
            'name':std_obj.name,
            'rollno':std_obj.rollno,
            'marks':std_obj.marks,
            'gf':std_obj.gf,
            'bf':std_obj.bf
        }
        old_data.update(new_data)
        form = StudentForm(old_data, instance=std_obj)
        if form.is_valid():
            form.save(commit=True)
            json_string = json.dumps({'msg':'Record Udated!'})
            return self.render_to_http_response(json_string)
        if form.errors:
            json_string = json.dumps(form.errors)
            return self.render_to_http_response(json_string, status=400)


    def delete(self,request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            json_string = json.dumps({'msg':'Please Enter Data in only JSON Format'})
            return self.render_to_http_response(json_string, status= 400)
        p_dict = json.loads(data)
        id = p_dict.get('id',None)
        if id is None:
            json_string = json.dumps({'msg':' for updation, id is Mandatory!'})
            return self.render_to_http_response(json_string, status=400)
        std_obj = self.get_reosurce_by_id(id)
        if std_obj is None:
            json_string = json.dumps({'msg':'Record not Found with given id'})
            return self.render_to_http_response(json_string, status=404)

        status, item_obj = std_obj.delete()
        if status == 1:
            json_string = json.dumps({'msg':'Record Deleted!'})
            return self.render_to_http_response(json_string)
        json_string = json.dumps({'msg':'Try again after sometimes'})
        return self.render_to_http_response(json_string, status=400)