from django.shortcuts import render
from api.serializers import StudentSerializer
from api.models import Student
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
