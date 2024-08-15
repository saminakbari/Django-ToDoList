from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from ToDoListApp.models import Task, ToDoList


class CreateTask3(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "v3/v3_create_task_template.html"
    fields = ['title', 'description', 'priority', 'deadline']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        list_id = self.kwargs['list_id']
        to_do_list = ToDoList.objects.get(pk=list_id)
        form.instance.to_do_lists.add(to_do_list)
        self.success_url = "http://localhost:8000/v3/to-do-list/get/" + str(list_id) + "/"
        return super(CreateTask3, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        list_id = self.kwargs['list_id']
        self.success_url = "http://localhost:8000/v3/to-do-list/get/" + str(list_id) + "/"
        return super(CreateTask3, self).post(request)

    def get(self, request, *args, **kwargs):
        list_id = self.kwargs['list_id']
        self.success_url = "http://localhost:8000/v3/to-do-list/get/" + str(list_id) + "/"
        return super(CreateTask3, self).get(request)
