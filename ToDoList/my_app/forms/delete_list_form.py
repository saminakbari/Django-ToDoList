from django import forms


class DeleteListForm(forms.Form):
    list_id = forms.IntegerField()
