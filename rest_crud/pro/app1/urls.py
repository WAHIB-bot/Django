from django.urls import path
from .import views
from .views import StudentsApi, CourseApi
urlpatterns = [
    # path('students/', views.get_all_students, name='students'),
    # path('Courses/', views.get_all_Courses, name='students'),
    # path('course/<str:pk>', views.get_student_by_course, name='students'),
    # path('course/<str:pk>/student/<str:pk1>', views.get_specific_student_in_specific_course, name='students'),
    # path('stu_create/', views.stu_create, name='stu_create'),
    # path('course_create/', views.course_create, name='course_create'),
    # path('enroll/', views.enroll, name='enroll'),
    # path('course/<str:course_id>/student/<str:stu_id>/enroll', views.enroll_stu, name='enroll_stu'),
    # path('courses/<str:course_id>/update', views.update_course, name='update_course'),
    # path('students/<str:student_roll>/update', views.update_student, name='update_student'),
    # path('courses/<str:course_id>/delete', views.del_course, name='delete_course'),
    # path('students/<str:student_roll>/delete', views.del_student, name='delete_student'),

    path('students/', StudentsApi.as_view(), name='students'),#Get and Post students
    path('students/<str:student_roll>', StudentsApi.as_view(), name='students'),#Get specific student, put and delete students

    path('courses/', CourseApi.as_view(), name='courses'),#Get and Post Courses
    path('courses/<str:course_id>', CourseApi.as_view(), name='courses'),#Get specific Course, put and delete Courses


]