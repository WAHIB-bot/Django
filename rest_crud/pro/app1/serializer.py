from rest_framework import serializers
from .models import Course,Student,Enrollemnt

# Create your models here.
class Course_Serializer(serializers.Serializer):
    course_id = serializers.CharField(max_length=20)
    title = serializers.CharField(max_length=255)
    decsription = serializers.CharField(max_length=500)
    duration = serializers.DurationField()

    def create(self, validate_data):
        return Course.objects.create(**validate_data) 
    

class Student_Serializer(serializers.Serializer):
    roll = serializers.CharField()
    name = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Student.objects.create(**validate_data) 


class Enrollemnt_Serializer(serializers.Serializer):
    student = serializers.PrimaryKeyRelatedField(queryset = Student.objects.all())         
    course = serializers.PrimaryKeyRelatedField(queryset = Course.objects.all())
    date = serializers.DateField(read_only=True)

    def create(self, validate_data):
        return Enrollemnt.objects.create(**validate_data) 
    