import requests
import json

BASE_URL = 'http://localhost:8000/'
END_POINT = 'api/'

def get_resource(id):
    emp = {}
    if id is not None:
        emp = {
            'id':id
        }
    req = requests.get(BASE_URL+END_POINT, data=json.dumps(emp))
    print(f'Status Code: {req.status_code}')
    print(req.json())
# id = eval(input('Enter Id/None:'))
# get_resource(id)

def create_resource():
    emp = {
        'eno':'100',
        'ename':'Sunny',
        'esal':1000.0,
        'eaddr':'Mumbai'
    }
    req = requests.post(BASE_URL+END_POINT, data= json.dumps(emp))
    print(f'Status Code: {req.status_code}')
    print(req.json())
# create_resource()

def update_resource(id):
    emp={
        'id':id,
        'ename':'Sunny Leone'
    }
    req = requests.put(BASE_URL + END_POINT , data=json.dumps(emp))
    print(f'Status Code: {req.status_code}')
    print(req.json())

# id = eval(input('Enter Id/None:'))
# update_resource(id)

def delete_resource(id):
    emp={
        'id':id,
        }
    req = requests.delete(BASE_URL + END_POINT , data=json.dumps(emp))
    print(f'Status Code: {req.status_code}')
    print(req.json())

id = eval(input('Enter Id/None:'))
delete_resource(id)