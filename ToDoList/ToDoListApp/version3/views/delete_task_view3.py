from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import RedirectView

from ToDoListApp.models import Task, ToDoList


class DeleteTask3(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, **kwargs):
        task_id = self.kwargs["task_id"]
        list_id = self.kwargs["list_id"]
        to_do_list = ToDoList.objects.get(pk=list_id)
        task = Task.objects.get(pk=task_id)
        to_do_list.tasks.remove(task)
        return reverse_lazy("v3-get-list", kwargs={"list_id": list_id})
