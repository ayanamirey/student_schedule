from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import viewsets
from app.serializers.timetable import TimetableSerializer, TimetableCreateSerializer, MyUserUpdateSerializer
from app.models.timetable import Timetable
from authorization.models.users import MyUser


class TimeTableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return TimetableCreateSerializer

        return super().get_serializer_class()


class GroupAPIList(generics.ListAPIView):
    """Фильтрация по группам"""

    def list(self, request, *args, **kwargs):
        user_group = MyUser.objects.get(username=request.user)
        queryset = Timetable.objects.all().filter(group=user_group.group_id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    serializer_class = TimetableSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DayAPIList(generics.ListAPIView):
    """Фильтрация по дням недели"""

    def list(self, request, pk, *args, **kwargs):
        queryset = Timetable.objects.all().filter(day=pk)
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    serializer_class = TimetableSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TeacherAPIList(generics.ListAPIView):
    """Фильтрация учителей по id"""

    def list(self, request, pk, *args, **kwargs):
        queryset = Timetable.objects.all().filter(pair__teacher=pk)
        page = self.paginate_queryset(queryset)

        for i in queryset:
            # if queryset[i.teat] !=
            print(i.pair)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    serializer_class = TimetableSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserGroupUpdate(generics.UpdateAPIView):
    """Изменение группы пользователя"""
    queryset = MyUser.objects.all()
    serializer_class = MyUserUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)
