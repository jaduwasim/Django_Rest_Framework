from rest_framework import serializers
from .models import Employee

def multiple_of_100(value):
        print('validation by using validator')
        if value % 100 != 0:
            raise serializers.ValidationError('Salary should be Multiple of 1000')
        return value

class EmployeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=70)
    esal = serializers.FloatField(validators = [multiple_of_100,])
    eaddr = serializers.CharField(max_length =70)

    
    def validate_esal(self, value):
        print('Field level Validation')
        if value < 5000:
            raise serializers.ValidationError('Salary Should be Greater Equal Five Thousend!')
        return value
    
    def validate(self, attrs):
        print('object level validator')
        ename = attrs.get('ename')
        esal = attrs.get('esal')
        if ename.lower() == 'sunny':
            if esal < 50000:
                raise serializers.ValidationError('Sunny salayr should be greater then 50000!')
        return attrs
    
    def create(self, validated_data):
        return Employee.objects.create( **validated_data)

    def update(self, instance, validated_data):
        instance.eno = validated_data.get('eno', instance.eno)
        instance.ename = validated_data.get('ename', instance.ename)
        instance.esal = validated_data.get('esal', instance.esal)
        instance.eaddr = validated_data.get('eadd', instance.eaddr)
        instance.save()
        return instance