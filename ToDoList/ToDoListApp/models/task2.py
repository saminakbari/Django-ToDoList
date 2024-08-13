import re
from datetime import datetime
from sqlite3 import Date

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


def get_priority(priority_number):
    match priority_number:
        case '1':
            return 'High'
        case '2':
            return 'Medium'
        case '3':
            return 'Low'


def validate_title(title):
    if not re.match("^[a-zA-Z0-9_\\-]+$", title):
        raise ValidationError("The name can only contain letters, numbers, dashes and underlines.")


def validate_date(date):
    if not re.match("^\\d{4}-\\d{2}-\\d{2}$", str(date)):
        raise ValidationError("The date format must be: yyyy-mm-dd.")
    if date < Date.today():
        raise ValidationError("The deadline cannot be in pas.")


def validate_priority(priority):
    if not priority == '1' or priority == '2' or priority == '3':
        raise ValidationError("Priority error!!!!!!!!!")
        # TODO: correct this function


class Task2(models.Model):
    PRIORITY_CHOICES = (('1', 'High'), ('2', 'Medium'), ('3', 'Low'))

    title = models.CharField(max_length=100, verbose_name='عنوان',
                             null=False, default="new-task", validators=[validate_title])
    description = models.CharField(max_length=1000, verbose_name='توضیحات', null=False, default="")
    deadline = models.DateField(max_length=10, verbose_name='زمان سرسید',
                                null=False, default=datetime.now().date(), validators=[validate_date])
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES,
                                verbose_name='اولویت', null=False, default='2',
                                validators=[validate_priority])
    to_do_lists = models.ManyToManyField(to='ToDoListApp.ToDoList2', related_name='tasks',
                                         verbose_name='لیست‌ها', null=True)
    users_shared_with = models.ManyToManyField(to=User, related_name='tasks_shared_with_user',
                                               verbose_name='افرادی که با آنها به اشتراک گذاشته شده')
    owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, verbose_name='صاحب',
                              null=True)

    def __str__(self):
        return "task: " + self.title
