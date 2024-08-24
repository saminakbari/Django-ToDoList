from django import forms

from ToDoListApp.models import ToDoList


class ListModelForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ["title"]
