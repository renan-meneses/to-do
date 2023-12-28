from django.urls import include, path

from rest_framework import routers

from .viewsets import AccountsViewSet

router = routers.DefaultRouter()
router.register(r"", AccountsViewSet, "accounts")

urlpatterns = [path("", include(router.urls))]
