import requests
import json

BASE_URL ='http://localhost:8000/'
END_POINT = 'api/'

def create_resource():
    emp={
        'eno':300,
        'ename':'ravi',
        'esal':6000.0,
        'eaddr':'Mumbai'
    }
    req = requests.post(BASE_URL + END_POINT, data=json.dumps(emp))
    print(f'Status Code: {req.status_code}')
    print(req.json())

create_resource()

def get_resource(id):
    emp = {}
    if id is not None:
        emp = {
            'id':id
        }
    req = requests.get(BASE_URL + END_POINT , data=json.dumps(emp))
    print(f'Status Code: {req.status_code}')
    print(req.json())
# print('id for particular records and None for all')
# id = eval(input('Enter id/None:'))
# get_resource(id)

def update_resource(id):
    emp = {
        'id':id,
        'eno':200,
        'ename':'washim akram',
        'esal':50000.0
    }
    req = requests.put(BASE_URL + END_POINT , data=json.dumps(emp))
    print(f'Status Code: {req.status_code}')
    print(req.json())

# id = eval(input('Enter id/None:'))
# update_resource(id)