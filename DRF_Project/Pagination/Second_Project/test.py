import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Second_Project.settings')
import django
django.setup()

import random
from faker import Faker
from testapp.models import Employee

fake = Faker()

def populate(n):
    for i in range(n):
        feno = random.randint(1001,9999)
        fename = fake.name()
        fesal = random.randint(10000,20000)
        feaddr = fake.city()
        emp_record = Employee.objects.get_or_create(eno=feno, ename=fename, esal=fesal, eaddr=feaddr)
    print(f'{n} records inserted')

n = eval(input('Enter Number of Reocords:'))
populate(n)