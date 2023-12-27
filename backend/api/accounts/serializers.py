from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.accounts.models import UserManager

User = get_user_model()


class UserManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserManager
        fields = "user"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "full_name", "email", "groups")
