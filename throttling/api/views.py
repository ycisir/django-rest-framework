from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from api.custom_throttling import CustomRateThrottle # custom class

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle, CustomRateThrottle]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    # throttle_classes = [ScopedRateThrottle] # user for specific view
    # throttle_scope = 'test'


