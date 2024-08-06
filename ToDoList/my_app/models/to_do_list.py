from django.db import models

from my_app.models import MyUser


class ToDoList(models.Model):
    list_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    all_lists = models.Manager
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="to_do_lists", default=None)
