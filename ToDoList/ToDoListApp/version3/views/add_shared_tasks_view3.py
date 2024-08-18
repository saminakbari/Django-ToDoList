from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from ToDoListApp.models import ToDoList, Task


class AddSharedTasks3(LoginRequiredMixin, TemplateView):
    template_name = 'v3/v3_add_shared_tasks_template.html'

    def post(self, request, *args, **kwargs):
        list_id = kwargs['list_id']
        to_do_list = ToDoList.objects.get(id=list_id)
        task_id = request.POST['task_id']
        task = Task.objects.get(id=task_id)
        to_do_list.tasks.add(task)
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        list_id = self.kwargs['list_id']
        context = super().get_context_data()
        to_do_list = ToDoList.objects.get(id=list_id)
        context['to_do_list'] = to_do_list
        shared_tasks = self.request.user.tasks_shared_with_user.all()
        context['tasks'] = shared_tasks
        return context
