from rest_framework import serializers
from .model import course_model
class course_serializer(serializers.Serializer):
    tile = serializers.CharField(max_length=100)
    des = serializers.CharField(max_length=250)
    instructor = serializers.CharField(max_length=100)
    duration = serializers.DurationField()

# def create(self, validate_data):
#     return course_model.objects.create(**validate_data)    