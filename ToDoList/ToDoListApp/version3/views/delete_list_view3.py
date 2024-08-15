from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView

from ToDoListApp.models.to_do_list import ToDoList


class DeleteList3(LoginRequiredMixin, DeleteView):
    template_name = "v3_delete_list_template.html"
    model = ToDoList
    pk_url_kwarg = "list_id"
    success_url = "http://localhost:8000/v3/to-do-list/showall/"


