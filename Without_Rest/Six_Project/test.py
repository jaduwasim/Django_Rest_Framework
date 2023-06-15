import requests
import json
BASE_URL = 'http://localhost:8000/'
END_POINT = 'api/'

def create_resource():
    emp_data={
        'eno':600,
        'ename':'Ravi',
        'esal':6000.0,
        'eaddr':'Delhi'
    }
    resp = requests.post(BASE_URL+END_POINT, data=json.dumps(emp_data))
    r = resp.json()
    print(r)
create_resource()

def Update_Resource():
    id = input('Enter id:')
    emp_data = {
        'ename':'washim akram',
        'esal': 50000.0
    }
    resp = requests.put(BASE_URL+END_POINT + id + '/', data=json.dumps(emp_data))
    print(resp.json())
# Update_Resource()

def Delete_resource():
    id = input('Enter id:')
    resp = requests.delete(BASE_URL+END_POINT + id + '/')
    print(resp.json())
# Delete_resource()

    