import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Seprate_Api_Folder_Project.settings')
import django
django.setup()

from faker import Faker
from testapp.models import Employee
from random import randint
faker = Faker()

def Populate(n):
    for i in range(n):
        feno = randint(1001,9999)
        fename = faker.name()
        fesal = randint(10000,20000)
        feaddr = faker.city()
        emp = Employee.objects.get_or_create(eno=feno, ename=fename, esal=fesal, eaddr=feaddr)
    print(f'{n} records inserted!')
n = eval(input('Enter Number of Records:'))
Populate(n)