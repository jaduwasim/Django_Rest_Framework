import requests 
import json

BASE_URL = 'http://localhost:8000/'
END_POINT = 'api/'



def get_resource(id=None):
    emp = {}
    if id is not None:
        emp={
            'id':id
        }
    resp = requests.get(BASE_URL+END_POINT, data=json.dumps(emp))
    print(f'Status Code: {resp.status_code}')
    print(resp.json())
# id = eval(input('Enter id or None:'))
# get_resource(id)

def create_resource():
    emp_data ={
        'eno':500,
        'ename':'Sunny',
        'esal':50000.0,
        'eaddr':'Chennai'
    }
    req = requests.post(BASE_URL + END_POINT, data=json.dumps(emp_data))
    print(f'Status Code: {req.status_code}')
    print(req.json())

# create_resource()

def Update_resource(id):
    emp_data = {
        'id':id,
        'ename':'washim akram',
        'esal':50000.0
    }
    req = requests.put(BASE_URL + END_POINT, data=json.dumps(emp_data))
    print(f'Status Code: {req.status_code}')
    print(req.json())
# id = eval(input('Enter id:'))
# Update_resource(id)

def delete_resource(id):
    emp_data = {
        'id':id
    }
    req = requests.delete(BASE_URL + END_POINT , data=json.dumps(emp_data))
    print(f'Status Code: {req.status_code}')
    print(req.json())
id = eval(input('Enter id:'))
delete_resource(id)