from django.db import models

# Create your models here.
class Course(models.Model):
    course_id_model = models.CharField(max_length=10 , primary_key=True)
    title_model = models.CharField(max_length=255)
    desc_model = models.TextField()
    instructor_model = models.CharField(max_length=255)
    duration_model = models.DurationField()

class Student(models.Model):
    name_model = models.CharField(max_length=100)
    roll_model = models.IntegerField(primary_key=True)
    city_model = models.CharField(max_length=100)

class Enrollment(models.Model):
    student_model = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollment')
    course_model = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollment')
    enrollment_date = models.DateField(auto_now_add=True)
