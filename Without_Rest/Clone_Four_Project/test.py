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
get_resoure()