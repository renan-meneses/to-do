from rest_framework import serializers
from apps.tasks.models import TaskModel

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ("id", "title", "status", "description", "user")

