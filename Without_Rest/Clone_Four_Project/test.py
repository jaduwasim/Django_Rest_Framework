import json
import requests

BASE_URL = 'http://localhost:8000/'
END_POINT = 'api/'
# id = input('Enter id:')

def get_resoure():
    id = input('Enter id:')
    resp = requests.get(BASE_URL + END_POINT + id)
    # if resp.status_code == requests.codes.ok:
    print(resp.status_code)    
    data = resp.json()
    print(data)
    # else:
    # print('somthing goes wrong!!')
# get_resoure()

def create_resource():
    emp_dict = {
        'eno' : 700,
        'ename':'Ravi Teja',
        'esal':500000.0,
        'eaddr' : 'Mumbai'
    }
    post_request = requests.post(BASE_URL+END_POINT, data = json.dumps(emp_dict))

    print(post_request.status_code)
    # print(post_request.text) 
    print(post_request.json())
create_resource()

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

def delete_resources():
    id = input('Enter Id:')
    resp = requests.delete(BASE_URL+END_POINT + id + '/')
    r = resp.json()
    print(r)
# delete_resources()