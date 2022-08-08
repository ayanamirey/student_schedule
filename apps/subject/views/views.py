from rest_framework import generics, permissions
from rest_framework import viewsets
from subject.models.models import Subject
from subject.serializers.serializers import SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (permissions.IsAuthenticated,)
