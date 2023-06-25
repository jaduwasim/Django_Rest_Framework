import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','First_Project.settings')
import django
django.setup()

from testapp.models import Employee
from random import randint
from faker import *

faker = Faker()

def populate(n):
    for i in range(n):
        feno = randint(1001,9999)
        fename = faker.name()
        fesal = randint(100000,200000)
        feaddr = faker.city()
        emp_recor = Employee.objects.get_or_create(eno=feno, ename=fename, esal=fesal, eaddr=feaddr)
        print(f'{n} data inserted')
populate(120)