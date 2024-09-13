from django.urls import path
from .import views

urlpatterns = [
    path('students/', views.get_all_students, name='students'),
    path('course/<str:pk>', views.get_student_by_course, name='students'),
    path('course/<str:pk>/student/<str:pk1>', views.get_specific_student_in_specific_course, name='students'),
    path('stu_create/', views.stu_create, name='stu_create'),
    path('course_create/', views.course_create, name='course_create'),
    path('enroll/', views.enroll, name='enroll'),
]