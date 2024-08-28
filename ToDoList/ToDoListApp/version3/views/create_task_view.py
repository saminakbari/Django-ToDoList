from django.urls import reverse_lazy
from django.views.generic import CreateView

from ToDoListApp.forms.task_model_form import TaskModelForm
from ToDoListApp.models import Task, ToDoList


class CreateTaskView(CreateView):
    model = Task
    template_name = "v3/v3_create_task_template.html"
    form_class = TaskModelForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        list_id = self.kwargs["list_id"]
        task = form.save()
        to_do_list = ToDoList.objects.get(pk=list_id)
        task.to_do_lists.add(to_do_list)
        self.success_url = reverse_lazy("v3-get-list", kwargs={"list_id": list_id})
        return super(CreateTaskView, self).form_valid(form)
