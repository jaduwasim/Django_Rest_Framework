import requests

BASE_URL = 'http://localhost:8000/'
END_POINT = 'api/'

def get_response():
    id = input('Enter id:')
    resp = requests.get(BASE_URL + END_POINT + id)
    if resp.status_code == requests.codes.ok:
        print(f'Status Code: {resp.status_code}')
        data = resp.json()
        print(data)
    else:
        print('Something goes wrong!!!!!')
get_response()

def get_all_resource():
    resp = requests.get(BASE_URL + END_POINT)
    print(f'Status Code: {resp.status_code}')
    data = resp.json()
    print(data)
# get_all_resource()
