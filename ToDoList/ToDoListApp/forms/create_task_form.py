from django import forms

from ToDoListApp.models import Task


class CreateTaskForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    description = forms.CharField(label="Description", max_length=250, required=False)
    priority = forms.ChoiceField(widget=forms.Select(), label="Priority",
                                 choices=Task.PRIORITY_CHOICES, initial='2')
    deadline = forms.DateField(label="Deadline")

    # class Meta:
    #     models = Task2
    #     fields = ['title', 'description', 'priority', 'deadline']
