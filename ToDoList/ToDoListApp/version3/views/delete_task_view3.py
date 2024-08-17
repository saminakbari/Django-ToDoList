from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from ToDoListApp.models import Task


class DeleteTask3(LoginRequiredMixin, DeleteView):
    template_name = 'v3/v3_delete_task_template.html'
    model = Task
    pk_url_kwarg = 'task_id'

    def get_success_url(self):
        list_id = self.kwargs['list_id']
        return reverse_lazy('v3-get-list', kwargs={'list_id': list_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['to_do_list'] = self.object
        return context

