from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from ToDoListApp.models.to_do_list import ToDoList


class EditList3(LoginRequiredMixin, UpdateView):
    template_name = "v3_edit_list_title_template.html"
    fields = ["title"]
    model = ToDoList
    pk_url_kwarg = 'list_id'
    success_url = "http://localhost:8000/v3/to-do-list/showall/"

