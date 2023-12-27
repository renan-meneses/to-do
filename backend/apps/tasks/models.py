from django.contrib.auth import get_user_model
from django.db import models

from apps.utils.base_model import BaseModel

User = get_user_model()

class TaskModel(BaseModel):
    class Status(models.TextChoices):
        PENDING = "1", "Pending"
        COMPLETED = "2", "Completed"

    status = models.CharField(
        max_length=12, choices=Status.choices, default=Status.PENDING
    )
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=155)        
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_task",
        null=True,
        blank=True,
    )
    class Meta:
        verbose_name = ("task")
        verbose_name_plural = ("tasks")
        permissions = (
            ("list_tasks", "List trasks"),
            ("create_task", "Create trask"),
            ("update_task", "Update trask"),
            ("delete_task", "Delete trask"),
        )