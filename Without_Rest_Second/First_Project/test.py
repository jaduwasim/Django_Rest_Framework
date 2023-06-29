import requests
import json

BASE_URL = 'http://localhost:8000/'
END_POINT = 'api/'

def get_resource_by_id(id):
    resp = requests.get(BASE_URL + END_POINT + str(id) + '/')
    data = resp.json()
    print(data)
# id=eval(input('Enter id:'))
# get_resource_by_id(id)

def update_resource(id):
    emp_data ={
        'eno':100,
        'ename':'Sunny',
        'esal':10000,
        'eaddr':'Mumbai'
    }
    resp = requests.put(BASE_URL + END_POINT + str(id) + '/', data=json.dumps(emp_data))
    data = resp.json()
    print(data)
# id=eval(input('Enter id:'))
# update_resource(id)

def delete_resource(id):
    resp = requests.delete(BASE_URL + END_POINT + str(id) + '/')
    data = resp.json()
#     print(data)
# id=eval(input('Enter id:'))
# delete_resource(id)

def get_all_resources():
    resp = requests.get(BASE_URL + END_POINT)
    data = resp.json()
    print(data)
# get_all_resources()

def create_resource():
    emp_data ={
        'eno':100,
        'ename':'Sunny',
        'esal':10000,
        'eaddr':'Mumbai'
    }
    resp = requests.post(BASE_URL + END_POINT, data=json.dumps(emp_data))
    data = resp.json()
    print(data)
create_resource()