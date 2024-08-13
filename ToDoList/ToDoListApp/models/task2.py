from datetime import datetime
from sqlite3 import Date

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

    title = models.CharField(max_length=100, verbose_name='عنوان',
                             null=False, default="new-task", validators=)
    description = models.CharField(max_length=1000, verbose_name='توضیحات',
                                   null=False, default="", validators=)
    deadline = models.DateField(max_length=10, verbose_name='زمان سرسید',
                                null=False, default=datetime.now().date(), validators=)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES,
                                verbose_name='اولویت', null=False, default='2',
                                validators=)
    to_do_lists = models.ManyToManyField(to='ToDoListApp.ToDoList2', related_name='tasks',
                                         verbose_name='لیست‌ها', null=True, validators=)
    users_shared_with = models.ManyToManyField(to=User, related_name='tasks_shared_with_user',
                                               verbose_name='افرادی که تسک با آنها به اشتراک گذاشته شده',
                                               null=True, validators=)
    owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, verbose_name='صاحب',
                              null=True, validators=)

    def __str__(self):
        return "task: " + self.title


