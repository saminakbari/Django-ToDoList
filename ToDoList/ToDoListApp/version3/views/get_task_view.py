from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from ToDoListApp.models import Task
from ToDoListApp.models.task import get_priority


class GetTask(LoginRequiredMixin, DetailView):
    template_name = "v3/v3_get_task_template.html"
    model = Task
    pk_url_kwarg = "task_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.object
        context["task"] = task
        context["priority"] = get_priority(task.priority)
        return context
