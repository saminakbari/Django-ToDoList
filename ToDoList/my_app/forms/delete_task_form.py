from django import forms


class DeleteTaskForm(forms.Form):
    task_id = forms.IntegerField()
