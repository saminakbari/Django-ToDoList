from django import forms

from ToDoListApp.models import Task


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "deadline", "priority", "attachment"]
