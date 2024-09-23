from django.shortcuts import render
from .models import Student
from .serializer import Student_Serializer
from rest_framework.renderers  import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.

def get_student(request):
    student = Student.objects.all()
    serializer = Student_Serializer(student, many = True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def post_student(request):
    if request.method == "POST":
        data = json.loads(request.body)
        serializer = Student_Serializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg" : "data created"})
        return JsonResponse(serializer.errors)

@csrf_exempt
def put_student(request,id):
    if request.method == "PUT":
        try:
            student = Student.objects.get(roll = id)
        except student.DoesNotExist:
            return JsonResponse({"error" : "Student Does Not Exist"})

        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"error" : "invalid Json"})

        serializer = Student_Serializer(student, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg" : "record Updated"})        
        return JsonResponse(serializer.errors)
    
@csrf_exempt

def del_student(request,stu_roll):
    if request.method == "DELETE":
        try:
            student = Student.objects.get(roll = stu_roll)
        except Student.DoesNotExist:
            return JsonResponse({"error" : "Student does not exist"})
        
        student.delete()
        return JsonResponse({"msg" : "Student deleted Successfully"})