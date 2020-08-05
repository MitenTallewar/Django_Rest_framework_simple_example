from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from studapp.serializer import StudentSerializer
from studapp.models import Student
# Create your views here.
class StudentOperations(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
