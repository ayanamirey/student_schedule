from django.urls import path, include
from rest_framework.routers import DefaultRouter
from day.views.views import DayModelViewSet

router = DefaultRouter()
router.register('day', DayModelViewSet, 'day')

urlpatterns = [
    path('', include(router.urls)),
]
