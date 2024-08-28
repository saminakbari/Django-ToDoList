from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from ToDoListApp.forms.task_model_form import TaskModelForm
from ToDoListApp.models import Task


class EditTaskView(LoginRequiredMixin, UpdateView):
    template_name = "v3/v3_edit_task_template.html"
    model = Task
    pk_url_kwarg = "task_id"
    form_class = TaskModelForm

    def get_success_url(self):
        list_id = self.kwargs["list_id"]
        return reverse_lazy("v3-get-list", kwargs={"list_id": list_id})
