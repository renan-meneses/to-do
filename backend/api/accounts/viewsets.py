from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from api.accounts.serializers import UserSerializer
from apps.accounts.models import User


class AccountsViewSet(ModelViewSet):
    authentication_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "id",
        "full_name",
        "email",
    ]
    search_fields = ["id", "full_name", "email"]
    ordering_fields = ["id", "full_name", "email"]
