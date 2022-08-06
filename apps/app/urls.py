from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views.timetable import GroupAPIList, DayAPIList, TeacherAPIList, UserGroupUpdate, TimeTableViewSet

router = DefaultRouter()
router.register('timetable', TimeTableViewSet, 'timetable')

urlpatterns = [
    # Расписание
    path('', include(router.urls)),

    # Фильтрованные
    path('day/<int:pk>/', DayAPIList.as_view()),
    path('group/', GroupAPIList.as_view()),
    path('teacher/<int:pk>', TeacherAPIList.as_view()),

    # Изменение группы пользователя
    path('group_update/<int:pk>', UserGroupUpdate.as_view()),
]
