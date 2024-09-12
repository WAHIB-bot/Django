from django.shortcuts import render
from django.shortcuts import render
from .models import Student,Course,Enrollemnt
from .serializer import Course_Serializer, Student_Serializer, Enrollemnt_Serializer
from rest_framework.renderers  import JSONRenderer
from django.http import HttpResponse
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.

def get_all_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = Student_Serializer(students, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse(status = 405)

def get_student_by_course(request, id):
    if request.method == "GET":    
        try:
            course1 = Course.objects.get(course_id = id)
        except Course.DoesNotExist:
            return HttpResponse((JSONRenderer().render({"Error" : "Course Not Found"})),content_type="application/json")
        enrollments = Enrollemnt.objects.filter(course = course1)
        students = [enrollment.student for enrollment in enrollments]
        serializer = Student_Serializer(students, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = "application/json")
    else:
        return HttpResponse(status = 405)
    

# def get_specific_student_in_specific_course(request, c_id, s_id):
#     if request.method == "GET":    
#         try:
#             course = Course.objects.get(course_id = c_id)
#             student = Student.objects.get(roll = s_id)
#             enrollemnt = Enrollemnt.objects.get(course = course, student = student)
#         except Course.DoesNotExist:        
#             return HttpResponse(JSONRenderer().render({"Error" : "Course does not found"}), content_type='application/json')
#         except Student.DoesNotExist:        
#             return HttpResponse(JSONRenderer().render({"Error" : "Student does not found"}), content_tupe='application/json')
#         except Enrollemnt.DoesNotExist:        
#             return HttpResponse(JSONRenderer().render({"Error" : "Student does not found"}), content_tupe='application/json')
#         Serializer = Enrollemnt_Serializer(enrollemnt)
#         json_data = JSONRenderer().render(Serializer.data)
#         return HttpResponse(json_data, content_type='application/json')
#     else:
#         HttpResponse(status = 405)