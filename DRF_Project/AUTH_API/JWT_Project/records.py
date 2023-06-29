import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','JWT_Project.settings')
import django
django.setup()

from random import randint
from faker import Faker
from testapp.models import Employee

faker = Faker()

def Populate(n):
    for i in range(n):
        feno = randint(1001,9999)
        fename = faker.name()
        fesal = randint(10000,20000)
        feaddr = faker.city()
        emp = Employee.objects.get_or_create(eno=feno, ename=fename, esal=fesal, eaddr=feaddr)
    print(f'{n} Record Inserted!')
n=eval(input('Enter Number of Record to Insert:'))
Populate(n)