from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
        #we will get data from frontend in json format, 
        #which will be deserialized by serializer class to convert into
        #Python Native format