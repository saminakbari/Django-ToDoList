from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from ToDoListApp.models import ToDoList
from ToDoListApp.models.to_do_list2 import ToDoList2


class CreateList3(LoginRequiredMixin, CreateView):
    model = ToDoList2
    fields = ["title"]
    template_name = "v3_create_list_template.html"
    success_url = "http://localhost:8000/v3/to-do-list/showall/"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateList3, self).form_valid(form)

