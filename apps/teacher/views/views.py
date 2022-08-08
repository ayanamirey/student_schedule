from rest_framework import generics, permissions
from rest_framework import viewsets
from teacher.serializers.serializers import TeacherSerializer
from teacher.models.models import Teacher


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.IsAuthenticated,)
