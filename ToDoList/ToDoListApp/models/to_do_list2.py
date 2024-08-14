from django.contrib.auth.models import User
from django.db import models

from ToDoListApp.models.task2 import validate_title


class ToDoList2(models.Model):
    title = models.CharField(max_length=100, default="new-list", null=False,
                             verbose_name='عنوان', validators=[validate_title])
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name="to_do_lists", default=None, verbose_name='صاحب')
