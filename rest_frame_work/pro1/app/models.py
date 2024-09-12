from django.db import models

# Create your models here.
class course_model(models.Model):
    tile = models.CharField(max_length=100)
    des = models.CharField(max_length=250)
    instructor = models.CharField(max_length=100)
    duration = models.DurationField()