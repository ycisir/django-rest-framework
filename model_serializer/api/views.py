import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from api.models import Student
from api.serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):

    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)

        if id is not None:
            student = Student.objects.get(pk=id)
            serializer = StudentSerializer(student)
            return JsonResponse(serializer.data)
        else:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            return JsonResponse(serializer.data, safe=False)
        
    
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            resp = {'msg':'Data inserted!'}
            return JsonResponse(resp, safe=False)
        
        return JsonResponse(serializer.errors)
    

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(pk=id)
        # serializer = StudentSerializer(student, data=python_data)
        serializer = StudentSerializer(student, data=python_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            resp = {'msg':'Data updated!'}
            return JsonResponse(resp, safe=False)
        
        return JsonResponse(serializer.errors)
    

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(pk=id)
        student.delete()
        resp = {'msg':'Data deleted!'}
        return JsonResponse(resp, safe=False)

