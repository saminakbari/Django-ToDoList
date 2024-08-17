from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView

from ToDoListApp.forms.task_model_form import TaskModelForm
from ToDoListApp.models import Task, ToDoList


class CreateTask3(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "v3/v3_create_task_template.html"
    form_class = TaskModelForm
    success_url = ""

    def form_valid(self, form):
        form.instance.owner = self.request.user
        list_id = self.kwargs['list_id']
        to_do_list = ToDoList.objects.get(pk=list_id)
        form.instance.to_do_lists.add(to_do_list)
        # self.success_url = "http://localhost:8000/v3/to-do-list/get/" + str(list_id) + "/"
        reverse('v3-get-list', kwargs={'list_id': list_id})
        return super(CreateTask3, self).form_valid(form)
