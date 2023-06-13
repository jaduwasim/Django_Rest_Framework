import requests

try:
	BASE_URL = 'http://localhost:8000/'
	END_POINT = input('Enter END_POINT:')
	# END_POINT = 'apijson/'

	r = requests.get(BASE_URL + END_POINT)
	print('Type of Response:',type(r))
	print(f'r : {r}')
	data = r.json() #Here we get json data in the form of dict
	print(f'data: {data}')
	print()
	print('Data come from Django Application:')
	print(f"Employee No: {data['eno']}\nEmployee Name: {data['ename']}\nEmployee Salary: {data['esal']}\nEmployee Address: {data['eaddr']}")

except:
	print('Your Entered END_POINT is Not Valid')