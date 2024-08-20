from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions
from api.custom_permissions import MyPermission

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]


