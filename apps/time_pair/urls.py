from django.urls import path, include
from rest_framework.routers import DefaultRouter
from time_pair.views.views import TimeViewSet

router = DefaultRouter()
router.register('time', TimeViewSet, 'time')

urlpatterns = [
    path('', include(router.urls)),
]
