from django.urls import path

from app.views.timetable import TimeTableAPIList, TimeTableAPICreate, TimeTableAPIUpdate, \
    TimeTableAPIRetrieveDestroy, GroupAPIList, DayAPIList, TeacherAPIList, UserGroupUpdate

urlpatterns = [
    path('', TimeTableAPIList.as_view(), name='pair_list'),
    path('create/', TimeTableAPICreate.as_view(), name='pair_create'),
    path('update/<int:pk>/', TimeTableAPIUpdate.as_view(), name='pair_update'),
    path('detail_delete/<int:pk>/', TimeTableAPIRetrieveDestroy.as_view(), name='pair_detail_delete'),

    # Фильтрованные
    path('day/<int:pk>/', DayAPIList.as_view()),
    path('group/', GroupAPIList.as_view()),
    path('teacher/<int:pk>', TeacherAPIList.as_view()),

    # Изменение группы пользователя
    path('group_update/<int:pk>', UserGroupUpdate.as_view()),
]
