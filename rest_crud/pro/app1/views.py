from django.shortcuts import render
from django.shortcuts import render
from .models import Student,Course,Enrollemnt
from .serializer import Course_Serializer, Student_Serializer, Enrollemnt_Serializer
from rest_framework.renderers  import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.

# def get_all_Courses(request):
#     if request.method == 'GET':
#         students = Course.objects.all()
#         serializer = Course_Serializer(students, many = True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type="application/json")
#     else:
#         return HttpResponse(status = 405)
    

# def get_all_students(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = Student_Serializer(students, many = True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type="application/json")
#     else:
#         return HttpResponse(status = 405)

# def get_student_by_course(request, pk):
#     if request.method == "GET":    
#         try:
#             course1 = Course.objects.get(course_id = pk)
#         except Course.DoesNotExist:
#             return HttpResponse((JSONRenderer().render({"Error" : "Course Not Found"})),content_type="application/json")
#         enrollments = Enrollemnt.objects.filter(course = course1)
#         students = [enrollment.student for enrollment in enrollments]
#         serializer = Student_Serializer(students, many = True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type = "application/json")
#     else:
#         return HttpResponse(status = 405)
    

# def get_specific_student_in_specific_course(request, pk, pk1):
#     if request.method == "GET":    
#         try:
#             course = Course.objects.get(course_id = pk)
#             student = Student.objects.get(roll = pk1)
#             Enrollemnt.objects.get(course = course, student = student)
#         except Course.DoesNotExist:        
#             return HttpResponse(JSONRenderer().render({"Error" : "Course does not found"}), content_type='application/json')
#         except Student.DoesNotExist:        
#             return HttpResponse(JSONRenderer().render({"Error" : "Student does not found"}), content_tupe='application/json')
#         except Enrollemnt.DoesNotExist:        
#             return HttpResponse(JSONRenderer().render({"Error" : "Student does not found"}), content_tupe='application/json')
#         Serializer = Student_Serializer(student)
#         json_data = JSONRenderer().render(Serializer.data)
#         return HttpResponse(json_data, content_type='application/json')
#     else:
#         HttpResponse(status = 405)

# @csrf_exempt
# def stu_create(request):
#     if request.method == "POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = Student_Serializer(data = pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {"msg" : "Data created"}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = "application/json")
#         json_data = JSONRenderer().render(serializer.error_messages)
#         return HttpResponse(json_data, content_type = "application/json")  
          
# @csrf_exempt
# def course_create(request):
#     if request.method == "POST":
#         json_data = request.body
#         print("body data:", request.body)
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = Course_Serializer(data = pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {"msg" : "Data created"}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = "application/json")
#         json_data = JSONRenderer().render(serializer.error_messages)
#         return HttpResponse(json_data, content_type = "application/json")    

# @csrf_exempt
# def enroll(request):
#     if request.method == "POST":
#         data = request.body
#         stream = io.BytesIO(data)
#         pythondata = JSONParser().parse(stream)
#         course_id = pythondata["course"]
#         student_id = pythondata["student"]
#         try:
#             course = Course.objects.get(course_id = course_id)
#         except Course.DoesNotExist:
#             return HttpResponse(JSONRenderer().render({"Error" : "Course does not found"}), content_type='application/json')
      
#         try:
#             student = Student.objects.get(roll = student_id)
#         except Course.DoesNotExist:
#             return HttpResponse(JSONRenderer().render({"Error" : "Student does not found"}), content_type='application/json')
      
#         serializer = Enrollemnt_Serializer(data = pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {"msg" : "Data created"}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = "application/json")
#         json_data = JSONRenderer().render(serializer.error_messages)
#         return HttpResponse(json_data, content_type = "application/json") 
    
# @csrf_exempt
# def enroll_stu(request,stu_id,course_id):
#     if request.method == "POST":
#         try:
#             course = Course.objects.get(course_id = course_id)
#             student = Student.objects.get(roll = stu_id)
#         except Student.DoesNotExist:
#             return HttpResponse(JSONRenderer().render({"Error" : "Student does not found"}), content_type='application/json')                        
#         except Course.DoesNotExist:            
#             return HttpResponse(JSONRenderer().render({"Error" : "Course does not found"}), content_type='application/json')

#         try:
#             data = {
#                 "course" : course.course_id,
#                 "student" : student.roll 
#             }
#         except json.JSONcodeError:
#             return JsonResponse (('error : Invalid JSON'), status = 400)    

#         serializer = Enrollemnt_Serializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {"msg" : "Data created"}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = "application/json")
#         json_data = JSONRenderer().render(serializer.error_messages)
#         return HttpResponse(json_data, content_type = "application/json") 

# @csrf_exempt
# def update_student(request,student_roll):
#     if request.method == 'PUT':
#         try:
#             student = Student.objects.get(roll = student_roll)
#         except Student.DoesNotExist:
#             return JsonResponse({'error' : 'Student Not Found'})
#         try:
#             data = json.loads(request.body) 
#         except json.JSONDecodeError:
#             return JsonResponse({'error' : 'Invalid JSON'})
        
#         serializer = Student_Serializer(student, data = data, partial = True)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'message':'Student updated successfully'})
#         else:
#             return JsonResponse(serializer.errors, status = 400)
#     else:
#         return HttpResponse(status = 405)    

# @csrf_exempt        
# def update_course(request,course_id):
#     if request.method == 'PUT':
#         try:
#             course = Course.objects.get(course_id = course_id)
#         except Course.DoesNotExist:
#             return JsonResponse({'error' : 'Course Not Found'})
#         try:
#             data = json.loads(request.body) 
#         except json.JSONDecodeError:
#             return JsonResponse({'error' : 'Invalid JSON'})
        
#         serializer = Course_Serializer(course, data = data, partial = True)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'message':'Course updated successfully'})
#         else:
#             return JsonResponse(serializer.errors, status = 400)
#     else:
#         return HttpResponse(status = 405)    
    
# @csrf_exempt    
# def del_course(request, course_id):
#     if request.method == 'DELETE':
#         try:
#             course = Course.objects.get(course_id = course_id)
#         except Course.DoesNotExist:
#             return JsonResponse({"error":"Course Not Found"})
        
#         course.delete()
#         return JsonResponse({"message":"Course deleted Successfully"})
#     return HttpResponse(status = 405)


# @csrf_exempt    
# def del_student(request, student_roll):
#     if request.method == 'DELETE':
#         try:
#             student = Student.objects.get(roll = student_roll)
#         except Student.DoesNotExist:
#             return JsonResponse({"error":"Student Not Found"})
        
#         student.delete()
#         return JsonResponse({"message":"Student deleted Successfully"})
#     return HttpResponse(status = 405)

@method_decorator(csrf_exempt, name = 'dispatch')
class StudentsApi(View):
    def get(self, request, *arg, **kwarg):
        students = Student.objects.all()
        serializer = Student_Serializer(students, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")
 

    def get(self, request, *arg, **kwargs):
        print(arg)
        try:
            course1 = Course.objects.get(course_id = kwargs.get("course_id"))
        except Course.DoesNotExist:
            return HttpResponse((JSONRenderer().render({"Error" : "Course Not Found"})),content_type="application/json")
        enrollments = Enrollemnt.objects.filter(course = course1)
        students = [enrollment.student for enrollment in enrollments]
        serializer = Student_Serializer(students, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = "application/json")
        
    
    

    def get(self, request,*arg, **kwargs):
        print("kwargs",kwargs)
        print(arg)
        try:
            course = Course.objects.get(course_id = kwargs.get("course_id"))
            student = Student.objects.get(roll = kwargs.get("stu_id"))
            Enrollemnt.objects.get(course = course, student = student)
        except Course.DoesNotExist:        
            return HttpResponse(JSONRenderer().render({"Error" : "Course does not found"}), content_type='application/json')
        except Student.DoesNotExist:        
            return HttpResponse(JSONRenderer().render({"Error" : "Student does not found"}), content_type='application/json')
        except Enrollemnt.DoesNotExist:        
            return HttpResponse(JSONRenderer().render({"Error" : "Student does not found"}), content_tupe='application/json')
        Serializer = Student_Serializer(student)
        json_data = JSONRenderer().render(Serializer.data)
        return HttpResponse(json_data, content_type='application/json')
 
    
    # def post(self, request,*arg, **kwargs):
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     serializer = Student_Serializer(data = pythondata)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res = {"msg" : "Data created"}
    #         json_data = JSONRenderer().render(res)
    #         return HttpResponse(json_data, content_type = "application/json")
    #     json_data = JSONRenderer().render(serializer.error_messages)
    #     return HttpResponse(json_data, content_type = "application/json")  