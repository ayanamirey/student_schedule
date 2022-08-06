from django.urls import path, include
from rest_framework.routers import DefaultRouter
from subject.views.views import SubjectViewSet

router = DefaultRouter()
router.register('subject', SubjectViewSet, 'subject')

urlpatterns = [
    path('', include(router.urls)),
]
