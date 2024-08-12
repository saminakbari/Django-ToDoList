from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from ToDoListApp.models.to_do_list2 import ToDoList2


class GetList3(LoginRequiredMixin, TemplateView):
    template_name = "v3_get_list_template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_id = self.kwargs['list_id']
        print(list_id)
        to_do_list = ToDoList2.objects.get(pk=list_id)
        context['tasks'] = to_do_list.tasks.all()
        context['to_do_list'] = to_do_list
        return context

