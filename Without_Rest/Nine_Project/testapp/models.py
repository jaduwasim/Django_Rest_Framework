from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    rollno = models.IntegerField()
    marks = models.IntegerField()
    gf = models.CharField(max_length=70)
    bf = models.CharField(max_length=70)