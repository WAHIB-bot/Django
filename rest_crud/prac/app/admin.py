from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class students_admin(admin.ModelAdmin):
    list_display = ('roll','name','city')
