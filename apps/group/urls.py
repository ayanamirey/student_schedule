from django.urls import path, include
from rest_framework.routers import DefaultRouter
from group.views.views import GroupViewSet

router = DefaultRouter()
router.register('group', GroupViewSet, 'group')

urlpatterns = [
    path('', include(router.urls)),
]
