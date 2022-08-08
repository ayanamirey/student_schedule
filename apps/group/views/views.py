from rest_framework import generics, permissions
from rest_framework import viewsets
from group.models.models import Group
from group.serializers.serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)
