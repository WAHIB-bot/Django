from django.urls import path
from .import views

urlpatterns = [
    path('students/', views.get_all_students, name='students'),
    path('course/<str:id>', views.get_student_by_course, name='students'),
    # path('course/<str:id>/student/<str:id>', views.get_specific_student_in_specific_course, name='students')
]