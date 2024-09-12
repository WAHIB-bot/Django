from django.urls import path
from .import views

urlpatterns = [
    path('course_list', views.course_list, name='course_list'),
    path('course_details/<int:id>', views.course_details, name='course_details'),
]