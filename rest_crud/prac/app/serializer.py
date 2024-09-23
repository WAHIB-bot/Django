from rest_framework import serializers
from .models import Student

class Student_Serializer(serializers.Serializer):
    roll = serializers.CharField()
    name = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Student.objects.create(**validate_data) 
    
    def update(self, instance, validate_data):
        instance.roll =  validate_data.get('roll', instance.roll)
        instance.name =  validate_data.get('name', instance.name)
        instance.city =  validate_data.get('city', instance.city)
        instance.save()
        return instance