from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=20)
    title = models.CharField(max_length=255)
    decsription = models.CharField(max_length=500)
    duration = models.DurationField()

class Student(models.Model):
    roll = models.CharField(unique=True, primary_key=True, max_length=20)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

class Enrollemnt(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollment')         
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollment')
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')         