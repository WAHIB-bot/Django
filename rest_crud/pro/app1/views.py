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

def get_student_by_course(request, pk):
    if request.method == "GET":    
        try:
            course1 = Course.objects.get(course_id = pk)
        except Course.DoesNotExist:
            return HttpResponse((JSONRenderer().render({"Error" : "Course Not Found"})),content_type="application/json")
        enrollments = Enrollemnt.objects.filter(course = course1)
        students = [enrollment.student for enrollment in enrollments]
        serializer = Student_Serializer(students, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = "application/json")
    else:
        return HttpResponse(status = 405)
    

def get_specific_student_in_specific_course(request, pk, pk1):
    if request.method == "GET":    
        try:
            course = Course.objects.get(course_id = pk)
            student = Student.objects.get(roll = pk1)
            Enrollemnt.objects.get(course = course, student = student)
        except Course.DoesNotExist:        
            return HttpResponse(JSONRenderer().render({"Error" : "Course does not found"}), content_type='application/json')
        except Student.DoesNotExist:        
            return HttpResponse(JSONRenderer().render({"Error" : "Student does not found"}), content_tupe='application/json')
        except Enrollemnt.DoesNotExist:        
            return HttpResponse(JSONRenderer().render({"Error" : "Student does not found"}), content_tupe='application/json')
        Serializer = Student_Serializer(student)
        json_data = JSONRenderer().render(Serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    else:
        HttpResponse(status = 405)

@csrf_exempt
def stu_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = Student_Serializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg" : "Data created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = "application/json")
        json_data = JSONRenderer().render(serializer.error_messages)
        return HttpResponse(json_data, content_type = "application/json")  
          
@csrf_exempt
def course_create(request):
    if request.method == "POST":
        json_data = request.body
        print("body data:", request.body)
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = Course_Serializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg" : "Data created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = "application/json")
        json_data = JSONRenderer().render(serializer.error_messages)
        return HttpResponse(json_data, content_type = "application/json")    

@csrf_exempt
def enroll(request):
    if request.method == "POST":
        data = request.body
        stream = io.BytesIO(data)
        pythondata = JSONParser().parse(stream)
        course_id = pythondata["course"]
        student_id = pythondata["student"]
        try:
            course = Course.objects.get(course_id = course_id)
        except Course.DoesNotExist:
            return HttpResponse(JSONRenderer().render({"Error" : "Course does not found"}), content_type='application/json')
      
        try:
            student = Student.objects.get(roll = student_id)
        except Course.DoesNotExist:
            return HttpResponse(JSONRenderer().render({"Error" : "Student does not found"}), content_type='application/json')
      
        serializer = Enrollemnt_Serializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg" : "Data created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = "application/json")
        json_data = JSONRenderer().render(serializer.error_messages)
        return HttpResponse(json_data, content_type = "application/json") 