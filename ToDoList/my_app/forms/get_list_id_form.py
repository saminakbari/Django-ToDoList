from django import forms


class GetListForm(forms.Form):
    list_id = forms.IntegerField()

