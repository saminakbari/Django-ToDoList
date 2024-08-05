from django.db import models


class ToDoList(models.Model):
    list_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    all_lists = models.Manager
