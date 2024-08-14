from django import forms


class CreateListForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100, required=False)

    def get_title(self):
        return self.cleaned_data['title']
