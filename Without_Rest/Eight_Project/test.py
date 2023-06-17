import requests
import json

BASE_URL = 'http://localhost:8000/'
END_POINT = 'api/'

def get_record(id=None):
    emp = {}
    if id is not None:
        emp = {
            'id':id
        }
    resp = requests.get(BASE_URL + END_POINT , data = json.dumps(emp))
    print(resp.json())
# get_record(2)

def create_record():
    emp = {
        'eno':'500',
        'ename':'Ravi',
        'esal':5000,
        'eaddr':'Bihar'
    }
    resp = requests.post(BASE_URL + END_POINT , data = json.dumps(emp))
    print(resp.json())
# create_record()

def Update_resource(id):
    emp_data = {
        'id':id,
        'ename':'washim akram',
        'esal': 50000.0
    }
    req = requests.put(BASE_URL + END_POINT, data= json.dumps(emp_data))
    print(req.json())
# id = int(input('Enter id:'))
# Update_resource(id)


def delete_resource(id):
    emp_data = {
        'id':id,
    }
    req = requests.delete(BASE_URL + END_POINT, data= json.dumps(emp_data))
    print(req.json())
id = int(input('Enter id:'))
delete_resource(id)