from rest_framework import generics, permissions
from rest_framework import viewsets
from day.models.models import DayOfTheWeek
from day.serializers.serializers import DayOfTheWeekSerializer


class DayModelViewSet(viewsets.ModelViewSet):
    queryset = DayOfTheWeek.objects.all()
    serializer_class = DayOfTheWeekSerializer
    permission_classes = (permissions.IsAuthenticated,)
