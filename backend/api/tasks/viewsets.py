from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from api.tasks.serializers import TaskSerializer
from apps.tasks.models import TaskModel
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(ModelViewSet):

    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "id",
        "user",
        "status",
    ]
    search_fields = ["id","user","status",]
    ordering_fields = ["id","user","status",]
