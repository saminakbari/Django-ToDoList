from django.db import models

from my_app.models import MyUser


class Task(models.Model):
    class Priority(models.TextChoices):
        HIGH = '1'
        MEDIUM = '2'
        LOW = '3'

    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    deadline = models.DateField()
    priority = models.CharField(max_length=1, choices=Priority.choices, default=Priority.MEDIUM)
    to_do_lists = models.ManyToManyField(to='my_app.ToDoList', related_name='tasks')
    all_tasks = models.Manager
    users_shared_with = models.ManyToManyField(to=MyUser, related_name='tasks_shared_with_user')
    owner = models.ForeignKey(to=MyUser, on_delete=models.SET_NULL, null=True)
