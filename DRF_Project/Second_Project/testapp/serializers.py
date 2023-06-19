from rest_framework import serializers
from .models import Employee

def Multiple_of_1000(value):
    print('By using Validators')
    if value % 1000 != 0:
        raise serializers.ValidationError('Salary shuld be Multiple of 1000!')
    return value

class EmployeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=70)
    esal = serializers.FloatField(validators = [Multiple_of_1000,])
    eaddr = serializers.CharField(max_length=70)


    def validate_esal(self, value):
        print('Field Level Validaton')
        if value < 5000:
            raise serializers.ValidationError('Slaray Should be grater than 5000!')
        return value
    
    def validate(self, attrs):
        print('object level validation')
        ename = attrs.get('ename')
        esal = attrs.get('esal')
        if ename.lower() == 'washim':
            if esal < 60000:
                raise serializers.ValidationError('Washim Salary Should be Mininmum 60k!')
        return attrs

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.eno = validated_data.get('eno', instance.eno)
        instance.ename = validated_data.get('ename',instance.ename)
        instance.esal = validated_data.get('esal',instance.esal)
        instance.eaddr = validated_data.get('eaddr',instance.eaddr)
        instance.save()
        return instance