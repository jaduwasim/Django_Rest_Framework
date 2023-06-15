import requests 
import json
BASE_URL = 'http://localhost:8000/'
END_POINT = 'api/'

def get_request_by_id():
    id = input('Enter Id:')
    resp = requests.get(BASE_URL + END_POINT + id + '/')
    r = resp.json()
    print(r)
# get_request_by_id()

def get_all_resource():
    resp = requests.get(BASE_URL + END_POINT)
    r = resp.json()
    print(r)

# get_all_resource()

def Update_Resource():
    id = input('Enter id:')
    emp = {
        'ename':'Washim akram',
        'esal' : 500000.0
    }
    resp = requests.put(BASE_URL + END_POINT + id +'/' , data=json.dumps(emp))
    put_request = resp.json()
    print(put_request)

# Update_Resource()

def delete_resource():
    id = input('Enter id:')
    resp = requests.delete(BASE_URL + END_POINT + id + '/')
    print(resp.json())
delete_resource()
