from django.contrib import admin
from .models import course_model
# Register your models here.
@admin.register(course_model)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("tile", "des", "instructor", "duration")