from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pair.views.views import PairViewSet

router = DefaultRouter()
router.register('pair', PairViewSet, 'pair')

urlpatterns = [
    path('', include(router.urls)),
]
