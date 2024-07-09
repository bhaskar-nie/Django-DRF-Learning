from .models import *
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    #type 3 validators
    def start_with_r(value):
        if(value[0].lower()!='r'):
            raise serializers.ValidationError('Name should start with R')
    
    name=serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

    
    #field Validation
    def validate_roll(self, value):
        if value>200:
            raise serializers.ValidationError('Seat Full')
        return value

    #Object Validation
    def validate(self, data):
        nm=data.get('name')
        ct=data.get('city')

        if(nm.lower()=='rohit' and ct.lower()!='mysuru'):
            raise serializers.ValidationError('Rohit belongs to Mysuru')
        
        return data

    
