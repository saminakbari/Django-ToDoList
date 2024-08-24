from django import forms

from ToDoListApp.models.task import Task, validate_date, validate_title


class TaskForm(forms.Form):
    title = forms.CharField(
        label="Title", max_length=100, validators=[validate_title], required=False
    )

    description = forms.CharField(label="Description", max_length=250, required=False)

    priority = forms.ChoiceField(
        widget=forms.Select(),
        label="Priority",
        choices=Task.PRIORITY_CHOICES,
        initial="2",
    )

    deadline = forms.DateField(
        label="Deadline", validators=[validate_date], required=False
    )

    attachment = forms.FileField(label="Attachment", required=False)
