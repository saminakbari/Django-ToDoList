from django import forms


class ListForm(forms.Form):
    title = forms.CharField(label="Title: ", max_length=100, required=False)
