from api.models import Student
from api.serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse

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
