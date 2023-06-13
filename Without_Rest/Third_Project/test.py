import requests

BASE_URL = 'http://localhost:8000/'
END_POINT = 'api/'
id = input('Enter Id:')

resp = requests.get(BASE_URL + END_POINT + id)
print(f'Current Status Code: {resp.status_code}')
emp_dict = resp.json()
print(emp_dict)

print('Employee Data:')
print(f"Employee eno:{emp_dict['eno']},Employee Name:{emp_dict['ename']}, Employee Salary:{emp_dict['esal']},Employee Address:{emp_dict['eaddr']}")