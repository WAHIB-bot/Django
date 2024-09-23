from django.db import models

# Create your models here.\

class Student(models.Model):
    roll = models.CharField(unique=True, primary_key=True, max_length=20)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)