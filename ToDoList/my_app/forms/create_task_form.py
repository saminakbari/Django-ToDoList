from django import forms


class CreateTaskForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    description = forms.CharField(label="Description", max_length=250)
    priority = forms.CharField(label="Priority", max_length=6)
    deadline = forms.DateField(label="Deadline")
