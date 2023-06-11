import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

def get_resources(id=None):
    data={}
    if id is not None:
        data={
            'id':id
            }
    resp=requests.get(BASE_URL+END_POINT, data=json.dumps(data))
    print('Status Code:',resp.status_code)
    print(resp.json())
# get_resources()
# get_resources(1)
# get_resources(2)
# get_resources(3)

def create_resource():
    new_emp={
        'eno':500,
        'ename':'Shanker',
        'esal':5000,
        'addr':'Bihar'
    }
    r=requests.post(BASE_URL+END_POINT, data=json.dumps(new_emp))
    print('Status Code:',r.status_code)
    print(r.json())

# create_resource()

def update_resource(id):
    new_data={
        'id':id,
        # 'eno':400,
        'ename':'Ravi',
        'esal':23000,
        'addr':'Chennai'
    }
    r=requests.put(BASE_URL+END_POINT, data=json.dumps(new_data))
    print('Status Code:',r.status_code)
    print(r.json())
# update_resource(4)


def partial_update(id):
    new_data={
        'id':id,
        # 'eno':400,
        # 'ename':'Ravi',
        'esal':88888,
        # 'addr':'Chennai'
    }
    r=requests.patch(BASE_URL+END_POINT, data=json.dumps(new_data))
    print('Status Code:',r.status_code)
    print(r.json())
# partial_update(4)

def delete_resource(id):
    data={
        'id':id
    }
    r=requests.delete(BASE_URL+END_POINT, data=json.dumps(data))
    print('Status Code:',r.status_code)
    print(r.json())
delete_resource(4)