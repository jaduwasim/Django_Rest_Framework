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
    print(resp.json())
# id = eval(input('Enter id or None:'))
# get_resource(id)

def create_resource():
    std={
        'name':'Washim akram',
        'rollno':104,
        'marks':90,
        'gf':'Malika',
        'bf':'Iqbla'
    }
    req = requests.post(BASE_URL+END_POINT, data=json.dumps(std))
    print(req.json())
# create_resource()

def update_resource(id=None):
    std={
        'id':id,
        'name':'Washim',
        'rollno':104,
        'marks':90,
        'gf':'Sunny',
        'bf':'azim'
    }
    req = requests.put(BASE_URL+END_POINT, data=json.dumps(std))
    print(req.json())
# id = eval(input('Enter id or None:'))
# update_resource(id)

def delete_resource(id=None):
    emp = {}
    if id is not None:
        emp={
            'id':id
        }
    resp = requests.delete(BASE_URL+END_POINT, data=json.dumps(emp))
    print(resp.json())
id = eval(input('Enter id or None:'))
delete_resource(id)