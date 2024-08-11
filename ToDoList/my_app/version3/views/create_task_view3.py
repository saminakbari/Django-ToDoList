from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from my_app.forms import CreateTaskForm
from my_app.models import Task2


class CreateTask3(LoginRequiredMixin, CreateView):
    model = Task2
    template_name = "v3_create_task_template.html"
    form_class = CreateTaskForm

    # def get(self, request, *args, **kwargs):
    #     list_id = self.kwargs['list_id']
    #     self.success_url = "http://localhost:8000/v3/to-do-list/get/" + str(list_id) + "/"
    #     return super(CreateTask3, self).get(request)
