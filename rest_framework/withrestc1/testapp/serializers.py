from rest_framework import serializers
from testapp.models import Employee
class EmployeeSerializer(serializers.Serializer):
    eno=serializers.IntegerField()
    ename=serializers.CharField(max_length=64)
    esal=serializers.FloatField()
    addr=serializers.CharField(max_length=64)
    def create(self,validated_data):
        return Employee.objects.create(**validated_data)
    def update(self,instance, validated_data):
        instance.eno=validated_data.get('eno',instance.eno)
        instance.ename=validated_data.get('ename',instance.ename)
        instance.esal=validated_data.get('esal',instance.esal)
        instance.addr=validated_data.get('addr',instance.addr)
        instance.save()
        return instance