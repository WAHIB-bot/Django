from django.shortcuts import render
from .models import course_model
from .serializer import course_serializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
# Create your views here.

def course_details(request,id):
    
    course = course_model.objects.get(id = id)
    serializer = course_serializer(course)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = "application/json")
    
        

def course_list(request):
    course = course_model.objects.all()
    serializer = course_serializer(course, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = "application/json")

# @csrf_exempt
# def stu_create(request):
#     if request.method == "POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {"msg" : "Data created"}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = "application/json")
#         json_data = JSONRenderer().render(serializer.error_messages)
#         return HttpResponse(json_data, content_type = "application/json")