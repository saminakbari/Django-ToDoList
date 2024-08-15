from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView

from ToDoListApp.models.to_do_list import ToDoList
from ToDoListApp.version3.urls import v3_urlpatterns


class DeleteList3(LoginRequiredMixin, DeleteView):
    template_name = "v3/v3_delete_list_template.html"
    model = ToDoList
    pk_url_kwarg = "list_id"
    success_url = v3_urlpatterns.show_lists
