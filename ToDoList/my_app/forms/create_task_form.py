from django import forms

from my_app.models import Task, Task2


class CreateTaskForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    description = forms.CharField(label="Description", max_length=250)
    priority = forms.ChoiceField(widget=forms.Select(), label="Priority", choices=Task.PRIORITY_CHOICES, initial='2')
    deadline = forms.DateField(label="Deadline")

    class Meta:
        models = Task2
        fields = ['title', 'description', 'priority', 'deadline']
