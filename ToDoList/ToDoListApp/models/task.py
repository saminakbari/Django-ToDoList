import re

import django
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

VALID_TITLE_PATTERN = "^[a-zA-Z0-9_\\-]+$"
VALID_DATE_PATTERN = "^\\d{4}-\\d{2}-\\d{2}$"


def get_state(state):
    if state:
        return "Done"
    return "Not Done"


def get_priority(priority_number):
    match priority_number:
        case "1":
            return "High"
        case "2":
            return "Medium"
        case "3":
            return "Low"


def validate_title(title):
    if not re.match(VALID_TITLE_PATTERN, title):
        message = "The name can only contain letters, numbers, dashes and underlines."
        raise ValidationError(message)


def validate_date(date):
    if not re.match(VALID_DATE_PATTERN, str(date)):
        raise ValidationError("The date format must be: yyyy-mm-dd.")
    if date < django.utils.timezone.now().date():
        raise ValidationError("The deadline cannot be in the past!")


def validate_priority(priority):
    if not (priority == "1" or priority == "2" or priority == "3"):
        raise ValidationError("Priority can only be 'High', 'Low', or 'Medium'.")


class Task(models.Model):
    PRIORITY_CHOICES = (("1", "High"), ("2", "Medium"), ("3", "Low"))
    STATE_CHOICES = ((False, "Not Done"), (True, "Done"))

    title = models.CharField(
        max_length=100,
        verbose_name="عنوان",
        null=False,
        default="new-task",
        validators=[validate_title],
    )

    description = models.CharField(
        max_length=1000, verbose_name="توضیحات", null=False, default="", blank=True
    )

    deadline = models.DateField(
        max_length=10,
        verbose_name="زمان سرسید",
        null=False,
        default=django.utils.timezone.now().date(),
        validators=[validate_date],
    )

    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        verbose_name="اولویت",
        null=False,
        default="2",
        validators=[validate_priority],
    )

    to_do_lists = models.ManyToManyField(
        to="ToDoListApp.ToDoList", related_name="tasks", verbose_name="لیست‌ها"
    )

    users_shared_with = models.ManyToManyField(
        to=User,
        related_name="tasks_shared_with_user",
        verbose_name="افرادی که با آنها به اشتراک گذاشته شده",
    )

    owner = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        verbose_name="صاحب تسک",
        null=True,
        related_name="tasks",
    )

    attachment = models.FileField(
        verbose_name="فایل ضمیمه", null=True, blank=True, upload_to="media_files"
    )

    state = models.BooleanField(
        verbose_name="وضعیت", choices=STATE_CHOICES, default=False
    )

    users_who_can_see = models.ManyToManyField(
        to=User,
        verbose_name="کاربرانی که فقط تسک را می‌بینند",
        null=True,
        related_name="shared_added_tasks",
    )

    class Meta:
        ordering = ["deadline", "priority"]

    def __str__(self):
        return "task: " + self.title
