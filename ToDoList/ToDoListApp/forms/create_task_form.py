from django import forms

from ToDoListApp.models import Task
from ToDoListApp.models.task2 import validate_title, validate_date


class CreateTaskForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100, validators=[validate_title])
    description = forms.CharField(label="Description", max_length=250, required=False)
    priority = forms.ChoiceField(widget=forms.Select(), label="Priority",
                                 choices=Task.PRIORITY_CHOICES, initial='2')
    deadline = forms.DateField(label="Deadline", validators=[validate_date])
