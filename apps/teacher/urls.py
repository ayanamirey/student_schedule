from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teacher.views.views import TeacherViewSet

router = DefaultRouter()
router.register('teacher', TeacherViewSet, 'teacher')

urlpatterns = [
    path('', include(router.urls)),
]