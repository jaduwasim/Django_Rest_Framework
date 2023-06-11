import requests
BASE_URL = 'http://127.0.0.1:8000/'
FIRST_ENDPOINT = 'api/'
SECOND_ENDPOINT = 'api2/'
THIRD_ENDPOINT = 'apimixinbyid/'
FOURTH_ENDPOINT = 'apilist'
FIFTH_ENDPONT = 'apimixinall/'

# ------------------------------------------------

def EmployeeDetaliCBV(id):
    print('EmployeeDetaliCBV:')
    resp = requests.get(BASE_URL+FIRST_ENDPOINT+id)
    print(resp)
    print('Status Code:',resp.status_code)
    print(resp.json())
# id = input('Enter your id:')
# EmployeeDetaliCBV(id)



# -------------------------------------------------
#'EmployeeListCBV2 based url: 
def EmployeeListCBV2():
    resp = requests.get(BASE_URL+SECOND_ENDPOINT+id)
    print(resp)
    print('Status Code:',resp.status_code)
    print(resp.json())
# id = input('Enter your id:')
# EmployeeListCBV2()
    
# ---------------------------------------------------
# EmployeeDetaliMixinCBV2 Based url

def EmployeeDetaliMixinCBV2(id):
    print('EmployeeDetaliMixinCBV2 Based url')
    resp = requests.get(BASE_URL+THIRD_ENDPOINT+id)
    print(resp)
    print('Status Code:',resp.status_code)
    print(resp.json())
# id = input('Enter your id:')
# EmployeeDetaliMixinCBV2(id)


# ---------------------------------------------------
#'EmployeeListCBV2 based url: 

def EmployeeListCBV2():
    print()
    print('*'*45)
    print('EmployeeListCBV2 based url:')
    resp = requests.get(BASE_URL+FOURTH_ENDPOINT)
    print('Status Code:',resp.status_code)
    print(resp.json())
# EmployeeListCBV2()

def EmployeeMixinCBV2():
    print()
    print('*'*45)
    print('EmployeeMixinCBV2 based url:')
    resp = requests.get(BASE_URL+FOURTH_ENDPOINT)
    print('Status Code:',resp.status_code)
    print(resp.json())
EmployeeMixinCBV2()
