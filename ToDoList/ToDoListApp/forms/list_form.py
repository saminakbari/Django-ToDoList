from django import forms

from ToDoListApp.models.task import validate_title


class ListForm(forms.Form):
    title = forms.CharField(label="Title: ", max_length=100, required=False, validators=[validate_title])
