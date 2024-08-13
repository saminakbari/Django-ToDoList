from django.contrib.auth.models import User
from django.db import models


class ToDoList2(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name="to_do_lists", default=None)