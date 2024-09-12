from rest_framework import serializers
from .models import Student,Course

class studentSerializers(serializers.Serializer):
    name_model = serializers.CharField(max_length=100)
    roll_model = serializers.IntegerField()
    city_model = serializers.CharField(max_length=100)

    # def create(self, validate_data):
    #     return Student.objects.create(**validate_data)

class courseSelizers(serializers.Serializer):
    course_id_model = serializers.CharField(max_length=10)
    title_model = serializers.CharField(max_length=255)
    desc_model = serializers.CharField()
    instructor_model = serializers.CharField(max_length=255)
    duration_model = serializers.DurationField()

class EnrollmentSerializer(serializers.Serializer):
    student_model = serializers.PrimaryKeyRelatedField(queryset = Student.objects.all())
    course_model = serializers.PrimaryKeyRelatedField(queryset = Course.objects.all())
    enrollment_date = serializers.DateField(read_only=True)    