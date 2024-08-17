from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from ToDoListApp.forms.list_model_form import ListModelForm
from ToDoListApp.models.to_do_list import ToDoList


class EditList3(LoginRequiredMixin, UpdateView):
    template_name = "v3/v3_edit_list_title_template.html"
    form_class = ListModelForm
    model = ToDoList
    pk_url_kwarg = 'list_id'
    success_url = reverse_lazy('v3-show-lists')

