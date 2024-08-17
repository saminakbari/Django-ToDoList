from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class AddSharedTasks3(LoginRequiredMixin, TemplateView):
    template_name = 'v3/v3_add_shared_tasks_template.html'

    
