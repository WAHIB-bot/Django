from django.contrib import admin
from .models import Student, Course, Enrollemnt
# Register your models here.
@admin.register(Student)
class students_admin(admin.ModelAdmin):
    list_display = ('roll','name','city')

@admin.register(Course)
class course_admin(admin.ModelAdmin):
    list_display = ('course_id','title','decsription','duration')   

@admin.register(Enrollemnt)
class enrollemnt_admin(admin.ModelAdmin):
    list_display = ('student','course','date')   
    search_fields = ('student_name','course_title')   
