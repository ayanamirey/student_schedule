from rest_framework import viewsets
from rest_framework import permissions
from pair.models.models import Pair
from pair.serializers.serializers import PairSerializer


class PairViewSet(viewsets.ModelViewSet):
    queryset = Pair.objects.all()
    serializer_class = PairSerializer
    permission_classes = (permissions.IsAuthenticated,)
