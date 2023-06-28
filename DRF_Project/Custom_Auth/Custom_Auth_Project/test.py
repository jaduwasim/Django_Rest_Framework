import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Custom_Auth_Project.settings')
import django
django.setup()

import random
from testapp.models import Employee
from faker import Faker
faker = Faker()

def populate(n):
    for i in range(n):
        feno = random.randint(1001,9999)
        fename = faker.name()
        fesal = random.randint(10000,20000)
        feaddr = faker.city()
        emp_record = Employee.objects.get_or_create(eno=feno, ename=fename, esal=fesal, eaddr=feaddr)

n = eval(input('Enter the Number of Records:'))
populate(n)
