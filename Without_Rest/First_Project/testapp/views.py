from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def EmployeeFirstViews(request):
    emp_data = {
        'eno':100,
        'ename' : 'Sunny',
        'esal' : 10000,
        'eaddr' : 'Mumbai'
    }
    resoponse = f"<h1>Employee No: {emp_data['eno']}<br>Employee Name: {emp_data['ename']}<br>Employee Salary: {emp_data['esal']}<br>Employee Address: {emp_data['eaddr']}</h1>"
    print(resoponse)
    return HttpResponse(resoponse)

# Here we are Using json inbuilt Module which are belong from Python 
import json
def EmployeeSecondViews(request):
    emp_data = {
        'eno':100,
        'ename' : 'Sunny',
        'esal' : 10000,
        'eaddr' : 'Mumbai'
    }
    emp_json = json.dumps(emp_data) #Converting python dict object to Json string object
    return HttpResponse(emp_json, content_type='appication/json')

# Django View Function to send JsonResponse directly:
# Here we are Using JsonResponse inbuilt Module which are belong from django.http import JsonResponse
def EmployeeThirdViews(request):
    emp_data = {
        'eno':100,
        'ename' : 'Sunny',
        'esal' : 10000,
        'eaddr' : 'Mumbai'
    }
    return JsonResponse(emp_data)

from django.views.generic import View

class EmloyeeCBV(View):
    def get(self, request, *agrs, **kwargs):
        return JsonResponse({'msg':'This Resopnse from GET Method'})
    
    def post(self, request, *args, **kwargs):
        return JsonResponse({'msg':'This Response from post Method'})

    def put(self, request, *args, **kwargs):
        return JsonResponse({'msg':'This Response from put Method'})
    
    def patch(self, request, *args, **kwargs):
        return JsonResponse({'msg':'This Response from pacth Method'})
    
    def delete(self, request, *args, **kwargs):
        return JsonResponse({'msg':'This Response from delete Method'})
    
    def Test(self, request, *args, **kwargs):
        return JsonResponse({'msg':'This Response from Test Method'})


