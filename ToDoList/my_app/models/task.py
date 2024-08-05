from django.db import models


class Task(models.Model):
    class Priority(models.TextChoices):
        HIGH = 'High'
        MEDIUM = 'Medium'
        LOW = 'Low'

    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    deadline = models.DateField()
    priority = models.CharField(max_length=6, choices=Priority.choices, default=Priority.MEDIUM)
    to_do_lists = models.ManyToManyField(to='my_app.ToDoList', related_name='tasks')
    all_tasks = models.Manager


