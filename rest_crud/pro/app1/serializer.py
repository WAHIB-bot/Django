from rest_framework import serializers
from .models import Course,Student,Enrollemnt

# Create your models here.

def validate_title(name):
    print("name:",name)
    if name[0].islower():
        raise serializers.ValidationError("title first letter must be capital...",)
    return name

def validate_decsription(name):
    count = len(name.split())
    if count < 10:
        raise serializers.ValidationError("Description is too short")
    return name


class Course_Serializer(serializers.Serializer):
    course_id = serializers.CharField(max_length=20)
    title = serializers.CharField(max_length=255, validators=[validate_title])
    decsription = serializers.CharField(max_length=500, validators = [validate_decsription])
    duration = serializers.DurationField()

    def create(self, validate_data):
        return Course.objects.create(**validate_data) 
    
    def update(self, instance, validate_data):
        instance.course_id =  validate_data.get('course_id', instance.course_id)
        instance.title =  validate_data.get('title', instance.title)
        instance.decsription =  validate_data.get('decsription', instance.decsription)
        instance.duration =  validate_data.get('duration', instance.duration)
        instance.save()
        return instance

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


class Enrollemnt_Serializer(serializers.Serializer):
    student = serializers.PrimaryKeyRelatedField(queryset = Student.objects.all())         
    course = serializers.PrimaryKeyRelatedField(queryset = Course.objects.all())
    date = serializers.DateField(read_only=True)

    def create(self, validate_data):
        return Enrollemnt.objects.create(**validate_data) 
    