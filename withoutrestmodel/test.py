import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api2/'
id = input('Enter your id:')
resp = requests.get(BASE_URL+ENDPOINT+id)
print(resp)
print('Status Code:',resp.status_code)
print(resp.json())

