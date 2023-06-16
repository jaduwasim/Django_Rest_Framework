import requests
import json

BASE_UR = 'http://localhost:8000/'
END_POINT =  'api/'

def create_resorce():
    emp_data ={
        'eno':600,
        'ename':'Pinny',
        'esal':600.0,
        'eaddr':'Delhi'
    }
    req = requests.post(BASE_UR+END_POINT, data=json.dumps(emp_data))
    print(req.json())
create_resorce()


def updat_resorce():
    id = input('Enter id:')
    emp_data ={
        'ename':'Washim Akram',
        'esal':50000.0,
    }
    req = requests.put(BASE_UR+END_POINT+id + '/', data=json.dumps(emp_data))
    print(req.json())

# updat_resorce()

def delete_resorce():
    id = input('Enter id:')
    req = requests.delete(BASE_UR+END_POINT+id + '/')
    print(req.json())

# delete_resorce()