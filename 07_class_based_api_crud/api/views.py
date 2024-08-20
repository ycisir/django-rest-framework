from django.shortcuts import render
from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView


class StudentApi(APIView):

    def get(self, request, pk, formant=None):
        if pk:
            student = Student.objects.get(id=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    

    def post(self, request, formant=None):
        serializer = StudentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Inserted'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, formant=None):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Updated'})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, formant=None):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Partially Updated'})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, formant=None):
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'message':'Data Deleted'})
        
