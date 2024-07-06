from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views import View
import io

# Model object - single object
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    # student = Student.objects.get(pk=pk)
    # print(student)
    serializer = StudentSerializer(student)
    # print(serializer)
    # print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

# Queryset - all data
def student_list(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)


class StudentCreate(View):
    def post(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser.parse(stream)
        serializer = StudentSerializer(python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data created'}
            return JsonResponse(res.data)
        else:
            