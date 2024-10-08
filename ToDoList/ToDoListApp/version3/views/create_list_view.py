from django.urls import reverse_lazy
from django.views.generic import CreateView

from ToDoListApp.forms.list_model_form import ListModelForm
from ToDoListApp.models.to_do_list import ToDoList


class CreateListView(CreateView):
    model = ToDoList
    template_name = "v3/v3_create_list_template.html"
    success_url = reverse_lazy("v3-show-lists")
    form_class = ListModelForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateListView, self).form_valid(form)
