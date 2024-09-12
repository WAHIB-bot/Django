from django.shortcuts import render
from .models import Student
from .serializer import studentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
def student_details(request,pk):
    stu = Student.objects.get(id=pk)
    serializer = studentSerializers(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = "application/json")

def student_list(request):
    stu = Student.objects.all()
    serializer = studentSerializers(stu, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = "application/json")

@csrf_exempt
def stu_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = studentSerializers(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg" : "Data created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = "application/json")
        json_data = JSONRenderer().render(serializer.error_messages)
        return HttpResponse(json_data, content_type = "application/json")
 