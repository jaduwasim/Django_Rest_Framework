import requests
import json

BASE_URL = 'http://localhost:8000/'
END_POINT = 'api/'

def get_resurce(id=None):
    emp_dict = {}
    if id is not None:
        emp_dict = {
            'id':id
        }
    resp = requests.get(BASE_URL + END_POINT, data=json.dumps(emp_dict))
    data = resp.json()
    print(data)
id=eval(input('Enter id:'))
get_resurce(id)