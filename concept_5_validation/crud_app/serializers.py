from .models import *
from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    #field Validation
    # def validate_roll(self, value):
    #     if value>200:
    #         raise serializers.ValidationError('Seat Full')
    #     return value

    #Object Validation
    def validate(self, data):
        nm=data.get('name')
        ct=data.get('city')

        if(nm.lower()=='chirag bansal' and ct.lower()!='kota'):
            raise serializers.ValidationError('Chirag belongs to Kota')
        
        return data

    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        #print(instance.name)
        instance.name=validated_data.get('name', instance.name)
        #print(instance.name)
        instance.roll=validated_data.get('roll', instance.roll)
        instance.city=validated_data.get('city', instance.city)
        instance.save()
        return instance

    
