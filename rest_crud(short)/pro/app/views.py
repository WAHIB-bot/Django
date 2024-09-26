from django.shortcuts import render
from .models import Student
from .serializer import student_serializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions 
# Create your views here.

class StudentModeViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = student_serializer
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [TokenAuthentication]

    # ------------------------------------------------------------------------------------

    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [IsAdminUser]

    # ------------------------------------------------------------------------------------