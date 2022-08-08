from rest_framework import generics, permissions
from rest_framework import viewsets
from time_pair.models.models import Time
from time_pair.serializers.serializers import TimeSerializer


class TimeViewSet(viewsets.ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    permission_classes = (permissions.IsAuthenticated,)
