from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from ToDoListApp.models.to_do_list import ToDoList


class DeleteList3(LoginRequiredMixin, DeleteView):
    template_name = "v3/v3_delete_list_template.html"
    model = ToDoList
    pk_url_kwarg = "list_id"
    success_url = reverse_lazy("v3-show-lists")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["to_do_list"] = self.object
        return context
