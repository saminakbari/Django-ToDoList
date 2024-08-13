from django.db import models

from ToDoListApp.models import MyUser


class ToDoList(models.Model):
    list_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE,
                              related_name="to_do_lists", default=None)
