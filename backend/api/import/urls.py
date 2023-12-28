from django.urls import include, path

from rest_framework import routers

from .viewsets import process_excel

router = routers.DefaultRouter()

urlpatterns = [
    path('', process_excel, name='process_excel')
               ]
