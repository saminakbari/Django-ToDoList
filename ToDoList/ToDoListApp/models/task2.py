from django.contrib.auth.models import User
from django.db import models


def get_priority(priority_number):
    match priority_number:
        case '1':
            return 'High'
        case '2':
            return 'Medium'
        case '3':
            return 'Low'


class Task2(models.Model):
    PRIORITY_CHOICES = (('1', 'High'), ('2', 'Medium'), ('3', 'Low'))
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, )
    deadline = models.DateField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    to_do_lists = models.ManyToManyField(to='ToDoListApp.ToDoList2', related_name='tasks')
    users_shared_with = models.ManyToManyField(to=User, related_name='tasks_shared_with_user')
    owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "task: " + self.title
