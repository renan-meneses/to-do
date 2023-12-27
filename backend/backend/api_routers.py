from django.urls import include, path  # noqa: F401

from rest_framework import routers  # noqa: F401

urlpatterns = [
    path("accounts/", include("api.accounts.urls")),
    path("tasks/", include("api.tasks.urls")),

]
