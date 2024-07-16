from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # specific permission
    # we can override this if its provided globally
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, AllowAny]
    permission_classes = [IsAdminUser]

