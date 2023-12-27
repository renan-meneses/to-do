from django.urls import include, path

from rest_framework import routers

from .viewsets import TaskViewSet

router = routers.DefaultRouter()
router.register(r"", TaskViewSet, "task")

urlpatterns = [path("", include(router.urls))]
