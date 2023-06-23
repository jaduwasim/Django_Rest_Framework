from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=70)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=70)

    class Meta:
        db_table = 'Employee'