import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from api.serializers import StudentSerializer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data inserted!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            return JsonResponse(serializer.errors)

