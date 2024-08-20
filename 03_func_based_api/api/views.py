from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view() #by default GET is here
def hello(request):
    return Response({'msg':'Hello yasir'})


@api_view(['GET', 'POST'])
def hello(request):
    if request.method == 'GET':
        # print(request.data)
        return Response({'msg':'This is get request'})
    
    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'This is post request', 'data':request.data})