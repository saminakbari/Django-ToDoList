from django.contrib.auth.models import User
from django.db import models

from ToDoListApp.models.task import validate_title


class ToDoList(models.Model):
    title = models.CharField(
        max_length=100,
        default="new-list",
        null=False,
        verbose_name="عنوان",
        validators=[validate_title],
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="to_do_lists",
        null=True,
        verbose_name="صاحب لیست",
    )

    def __str__(self):
        return "list: " + self.title
