from django import forms


class GetTaskForm(forms.Form):
    task_id = forms.IntegerField(widget=forms.HiddenInput())
